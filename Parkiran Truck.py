from datetime import datetime


# ==================== DATA AWAL ====================
# Setiap kunjungan memiliki ID unik.
# waktu_keluar kosong berarti kendaraan masih di garasi.
# Seluruh data berikut adalah contoh.

data_garasi = [
    {
        "id": "G001",
        "plat": "B 1234 ABC",
        "sopir": "Budi",
        "jenis": "CDD",
        "waktu_masuk": "07-10-2026 08:00",
        "waktu_keluar": ""
    },
    {
        "id": "G002",
        "plat": "D 5678 DEF",
        "sopir": "Andi",
        "jenis": "Fuso",
        "waktu_masuk": "07-10-2026 09:00",
        "waktu_keluar": ""
    },
    {
        "id": "G003",
        "plat": "B 9012 GHI",
        "sopir": "Dedi",
        "jenis": "Mobil",
        "waktu_masuk": "07-10-2026 07:00",
        "waktu_keluar": "07-10-2026 10:00"
    }
]


# ==================== FUNGSI BANTU ====================

def waktu_sekarang():
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def input_teks(pesan):
    while True:
        teks = input(pesan).strip()

        if teks != "":
            return teks

        print("Input tidak boleh kosong.")


def konfirmasi(pesan):
    while True:
        jawaban = input(pesan + " (y/n): ").strip().lower()

        if jawaban == "y":
            return True
        elif jawaban == "n":
            return False
        else:
            print("Masukkan y atau n.")


def pilih_jenis():
    jenis_kendaraan = {
        "1": "Mobil",
        "2": "CDD",
        "3": "Fuso",
        "4": "Wingbox",
        "5": "Trailer"
    }

    while True:
        print("\nJenis kendaraan:")

        for nomor, jenis in jenis_kendaraan.items():
            print(f"{nomor}. {jenis}")

        pilihan = input("Pilih jenis kendaraan: ").strip()

        if pilihan in jenis_kendaraan:
            return jenis_kendaraan[pilihan]

        print("Pilihan tidak valid.")


def cari_data(id_kunjungan):
    for kendaraan in data_garasi:
        if kendaraan["id"] == id_kunjungan.strip().upper():
            return kendaraan

    return None


def plat_masih_di_garasi(plat, abaikan_id=""):
    # Spasi dan huruf besar/kecil tidak memengaruhi pengecekan.
    plat_dicari = "".join(plat.upper().split())

    for kendaraan in data_garasi:
        plat_tersimpan = "".join(kendaraan["plat"].upper().split())

        if (
            plat_tersimpan == plat_dicari
            and kendaraan["waktu_keluar"] == ""
            and kendaraan["id"] != abaikan_id
        ):
            return True

    return False


def tampilkan_data(daftar):
    if not daftar:
        print("\nData tidak ditemukan.")
        return

    for kendaraan in daftar:
        print("-" * 45)
        print(f"ID kunjungan : {kendaraan['id']}")
        print(f"Nomor polisi : {kendaraan['plat']}")
        print(f"Nama sopir   : {kendaraan['sopir']}")
        print(f"Jenis        : {kendaraan['jenis']}")
        print(f"Waktu masuk  : {kendaraan['waktu_masuk']}")

        if kendaraan["waktu_keluar"] == "":
            print("Waktu keluar : -")
            print("Status       : DI GARASI")
        else:
            print(f"Waktu keluar : {kendaraan['waktu_keluar']}")
            print("Status       : SUDAH KELUAR")

    print("-" * 45)
    print(f"Jumlah catatan: {len(daftar)}")


# ==================== READ ====================

def read_data():
    while True:
        print("\n=== LIHAT DATA GARASI ===")
        print("1. Tampilkan semua catatan")
        print("2. Cari berdasarkan ID kunjungan")
        print("3. Tampilkan kendaraan di garasi")
        print("4. Kembali ke menu utama")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(data_garasi)

        elif pilihan == "2":
            id_kunjungan = input_teks("Masukkan ID kunjungan: ")
            kendaraan = cari_data(id_kunjungan)

            if kendaraan is None:
                print("ID kunjungan tidak ditemukan.")
            else:
                tampilkan_data([kendaraan])

        elif pilihan == "3":
            kendaraan_di_garasi = []

            for kendaraan in data_garasi:
                if kendaraan["waktu_keluar"] == "":
                    kendaraan_di_garasi.append(kendaraan)

            tampilkan_data(kendaraan_di_garasi)

        elif pilihan == "4":
            return

        else:
            print("Pilihan tidak valid.")


# ==================== CREATE ====================

def create_data():
    while True:
        print("\n=== KENDARAAN MASUK ===")
        print("1. Catat kendaraan masuk")
        print("2. Kembali ke menu utama")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "2":
            return

        if pilihan != "1":
            print("Pilihan tidak valid.")
            continue

        id_kunjungan = input_teks(
            "ID kunjungan baru (contoh G004): "
        ).upper()

        if cari_data(id_kunjungan) is not None:
            print("ID sudah digunakan. Gunakan ID lain.")
            continue

        plat = input_teks("Nomor polisi: ").upper()

        if plat_masih_di_garasi(plat):
            print("Kendaraan ini masih tercatat di dalam garasi.")
            continue

        sopir = input_teks("Nama sopir: ")
        jenis = pilih_jenis()

        kendaraan_baru = {
            "id": id_kunjungan,
            "plat": plat,
            "sopir": sopir,
            "jenis": jenis,
            "waktu_masuk": waktu_sekarang(),
            "waktu_keluar": ""
        }

        tampilkan_data([kendaraan_baru])

        if konfirmasi("Simpan catatan kendaraan masuk?"):
            data_garasi.append(kendaraan_baru)
            print("Kendaraan masuk berhasil dicatat.")
        else:
            print("Penambahan dibatalkan.")


# ==================== UPDATE ====================

def update_data():
    while True:
        print("\n=== UBAH DATA / KENDARAAN KELUAR ===")
        print("1. Pilih catatan yang akan diubah")
        print("2. Kembali ke menu utama")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "2":
            return

        if pilihan != "1":
            print("Pilihan tidak valid.")
            continue

        id_kunjungan = input_teks("Masukkan ID kunjungan: ")
        kendaraan = cari_data(id_kunjungan)

        if kendaraan is None:
            print("ID kunjungan tidak ditemukan.")
            continue

        tampilkan_data([kendaraan])

        if not konfirmasi("Lanjutkan perubahan?"):
            continue

        print("\n1. Ubah nomor polisi")
        print("2. Ubah nama sopir")
        print("3. Ubah jenis kendaraan")
        print("4. Catat kendaraan keluar")
        print("5. Batalkan")

        kolom = input("Pilih perubahan: ").strip()

        # Gunakan salinan agar data asli belum berubah
        # sebelum pengguna mengonfirmasi penyimpanan.
        data_baru = kendaraan.copy()

        if kolom == "1":
            plat_baru = input_teks("Nomor polisi baru: ").upper()

            # Untuk kendaraan yang masih di garasi,
            # nomor polisi tidak boleh sama dengan kendaraan aktif lain.
            if (
                kendaraan["waktu_keluar"] == ""
                and plat_masih_di_garasi(
                    plat_baru, kendaraan["id"]
                )
            ):
                print("Nomor polisi tersebut masih ada di garasi.")
                continue

            data_baru["plat"] = plat_baru

        elif kolom == "2":
            data_baru["sopir"] = input_teks("Nama sopir baru: ")

        elif kolom == "3":
            data_baru["jenis"] = pilih_jenis()

        elif kolom == "4":
            if kendaraan["waktu_keluar"] != "":
                print("Kendaraan ini sudah tercatat keluar.")
                continue

            waktu_keluar = waktu_sekarang()

            # Cegah waktu keluar lebih awal dari waktu masuk.
            masuk = datetime.strptime(
                kendaraan["waktu_masuk"], "%d-%m-%Y %H:%M"
            )
            keluar = datetime.strptime(
                waktu_keluar, "%d-%m-%Y %H:%M"
            )

            if keluar < masuk:
                print("Waktu keluar lebih awal dari waktu masuk.")
                print("Periksa tanggal dan jam komputer.")
                continue

            data_baru["waktu_keluar"] = waktu_keluar

        elif kolom == "5":
            continue

        else:
            print("Pilihan tidak valid.")
            continue

        tampilkan_data([data_baru])

        if konfirmasi("Simpan perubahan?"):
            kendaraan.update(data_baru)
            print("Data berhasil diperbarui.")
        else:
            print("Perubahan dibatalkan.")


# ==================== DELETE ====================

def delete_data():
    while True:
        print("\n=== HAPUS CATATAN ===")
        print("1. Hapus catatan kendaraan")
        print("2. Kembali ke menu utama")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "2":
            return

        if pilihan != "1":
            print("Pilihan tidak valid.")
            continue

        id_kunjungan = input_teks("Masukkan ID kunjungan: ")
        kendaraan = cari_data(id_kunjungan)

        if kendaraan is None:
            print("ID kunjungan tidak ditemukan.")
            continue

        tampilkan_data([kendaraan])

        if konfirmasi("Yakin ingin menghapus catatan ini?"):
            data_garasi.remove(kendaraan)
            print("Catatan berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")


# ==================== MENU UTAMA ====================

def menu_utama():
    while True:
        print("\n" + "=" * 45)
        print("    PENCATATAN KENDARAAN MASUK DAN KELUAR")
        print("                 GARASI")
        print("=" * 45)
        print("1. Lihat data kendaraan")
        print("2. Catat kendaraan masuk")
        print("3. Ubah data / catat kendaraan keluar")
        print("4. Hapus catatan kendaraan")
        print("5. Keluar dari program")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            read_data()

        elif pilihan == "2":
            create_data()

        elif pilihan == "3":
            update_data()

        elif pilihan == "4":
            delete_data()

        elif pilihan == "5":
            if konfirmasi(
                "Keluar dari program? Perubahan data akan hilang"
            ):
                print("Terima kasih. Program selesai.")
                break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")


if __name__ == "__main__":
    menu_utama()