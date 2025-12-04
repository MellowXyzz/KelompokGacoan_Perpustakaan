print("="*100)
print("Projek Akhir Praktikum Alpro 1A")
print("Program Perpustakaan")
print("="*100)

# ===============================================================#
perpustakaan = {}
pinjam = {}
kembali = {}

# =================== FUNGSI TAMBAHAN =========================== #

def validasi_tanggal_ddmmyyyy(tanggal):
    if len(tanggal) != 10:
        return False
    if tanggal[2] != '-' or tanggal[5] != '-':
        return False
    
    d, m, y = tanggal.split('-')
    if not (d.isdigit() and m.isdigit() and y.isdigit()):
        return False

    d = int(d); m = int(m); y = int(y)

    if not (1 <= m <= 12):
        return False

    hari_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if y % 4 == 0:
        hari_bulan[1] = 29

    if d < 1 or d > hari_bulan[m - 1]:
        return False
    
    return True


def hitung_denda(tgl_pinjam, tgl_kembali):

    if len(tgl_pinjam) != 10 or len(tgl_kembali) != 10:
        return "Format tanggal salah"
    if tgl_pinjam[2] != '-' or tgl_pinjam[5] != '-' or tgl_kembali[2] != '-' or tgl_kembali[5] != '-':
        return "Format tanggal salah"

    d1, m1, y1 = tgl_pinjam.split('-')
    d2, m2, y2 = tgl_kembali.split('-')

    if not (d1.isdigit() and m1.isdigit() and y1.isdigit() and
            d2.isdigit() and m2.isdigit() and y2.isdigit()):
        return "Format tanggal salah"

    d1 = int(d1); m1 = int(m1); y1 = int(y1)
    d2 = int(d2); m2 = int(m2); y2 = int(y2)

    total1 = y1 * 365 + m1 * 30 + d1
    total2 = y2 * 365 + m2 * 30 + d2

    selisih = total2 - total1
    if selisih < 0:
        return "Tanggal kembali tidak boleh lebih kecil dari tanggal pinjam"

    batas = 7
    denda_per_hari = 2000

    if selisih <= batas:
        return 0
    else:
        return (selisih - batas) * denda_per_hari


# =================== MENU UTAMA ================================ #

def menu_admin():
    print("===Menu Perpustakaan (Admin)===")
    print("1. Tampilkan Semua Buku")
    print("2. Cari Buku")
    print("3. Tambah Buku Baru")
    print("4. Update Buku")
    print("5. Hapus Buku")
    print("6. Peminjaman Buku")
    print("7. Data Peminjaman")
    print("8. Pengembalian Buku")
    print("9. Data Pengembalian Buku")
    print("10. Keluar")


def menu_user():
    print("===Menu Perpustakaan (User)===")
    print("1. Tampilkan Semua Buku")
    print("2. Cari Buku")
    print("3. Keluar")


def tampilkan():
    if not perpustakaan:
        print("Tidak ada buku tersimpan.")
    else:
        print("Daftar Buku:")
        for id, details in perpustakaan.items():
            print(f"ID: {id}, Nama Buku: {details[0]}, Penulis: {details[1]}, Tahun Terbit: {details[2]}")


def cari():
    nama = input("Masukkan nama Buku yang dicari: ").strip().lower()
    ketemu = False

    for id, details in perpustakaan.items():
        if details[0].lower() == nama:
            print(f"ID: {id}, Nama Buku: {details[0]}, Penulis: {details[1]}, Tahun Terbit: {details[2]}")
            ketemu = True
    if not ketemu:
        print("Barang tidak ditemukan.")


def tambah():
    id = input("Masukkan ID buku : ").strip()
    if id in perpustakaan:
        print("Buku dengan ID tersebut sudah ada.")
        return
    buku = input("Masukkan Nama Buku: ").strip()
    penulis = input("Masukkan Nama Penulis: ")
    tahun = input("Masukkan Tahun Terbit: ")

    if not (tahun.isdigit() and len(tahun) == 4):
        print("Tahun tidak valid. Harus berupa 4 digit angka.")
        return

    perpustakaan[id] = [buku, penulis, tahun]
    print("Buku berhasil ditambahkan.")


def update():
    id = input("Masukkan ID Buku yang ingin diperbarui : ").strip()
    if id in perpustakaan:
        buku_baru = input("Masukkan Nama Buku : ")
        penulis_baru = input("Masukkan Nama Penulis : ")
        tahun_baru = input("Masukkan Tahun Terbit : ")

        if not (tahun_baru.isdigit() and len(tahun_baru) == 4):
            print("Tahun tidak valid. Harus berupa 4 digit angka.")
            return
        
        perpustakaan[id] = [buku_baru, penulis_baru, tahun_baru]
        print("Buku berhasil diperbarui!")
    else:
        print("Buku tidak ditemukan!")


def hapus():
    id = input("Masukkan id buku yang ingin dihapus: ").strip()
    if id not in perpustakaan:
        print("Buku tidak ditemukan.")
        return
    del perpustakaan[id]
    print("Buku berhasil dihapus.")


def data_pinjam():
    if not pinjam:
        print("Tidak ada Peminjaman.")
    else:
        print("Daftar Pinjaman:")
        for id, details in pinjam.items():
            print(f"ID: {id}, Nama Peminjam: {details[0]}, No.Telepon: {details[1]}, "
                  f"Tanggal Pinjam: {details[2]}, ID Buku: {details[3]}, Nama Buku: {details[4]}")

def tambah_pinjam():
    id = input("Masukkan ID Peminjaman : ").strip()
    if id in pinjam:
        print("Pinjaman dengan ID tersebut sudah ada.")
        return

    nama = input("Masukkan Nama Peminjam: ").strip()

    while True:
        no = input("Masukkan No Telepon: ").strip()
        if no.isdigit() and len(no) <= 13:
            break
        print("Nomor telepon harus berupa angka dan maksimal 13 digit.\n")

    while True:
        tanggal = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY): ").strip()
        if validasi_tanggal_ddmmyyyy(tanggal):
            break
        print("Tanggal tidak valid. Silakan coba lagi.\n")

    if perpustakaan:
        print("Daftar Buku Tersedia:")
        for id_buku, details in perpustakaan.items():
            print(f"ID: {id_buku}, Nama Buku: {details[0]}")
    else:
        print("Tidak ada buku tersimpan.")
        return

    while True:
        buku = input("Masukkan nama buku yang dipinjam : ").strip().lower()
        buku_ada = False

        for id_buku, details in perpustakaan.items():
            if details[0].lower() == buku:
                buku_ada = True
                id_buku_pinjam = id_buku
                nama_buku_pinjam = details[0]
                penulis_pinjam = details[1]
                tahun_pinjam = details[2]
                break

        if buku_ada:
            break
        print("Buku tidak ditemukan. Silakan coba lagi.\n")

    del perpustakaan[id_buku_pinjam]

    pinjam[id] = [nama, no, tanggal, id_buku_pinjam, nama_buku_pinjam, penulis_pinjam, tahun_pinjam]
    print("Peminjaman berhasil ditambahkan.")


# =================== PERBAIKAN PENGEMBALIAN =================== #

def tambah_kembali():
    id_pinjam = input("Masukkan ID Peminjaman yang ingin dikembalikan: ").strip()
    if id_pinjam not in pinjam:
        print("Peminjaman dengan ID tersebut tidak ditemukan.")
        return
    
    while True:
        tanggal_kembali = input("Masukkan Tanggal Pengembalian (DD-MM-YYYY): ").strip()
        if validasi_tanggal_ddmmyyyy(tanggal_kembali):
            break
        print("Tanggal tidak valid. Silakan coba lagi.\n")

    details = pinjam[id_pinjam]
    nama = details[0]
    no = details[1]
    tanggal_pinjam = details[2]
    id_buku = details[3]
    nama_buku = details[4]
    penulis = details[5]
    tahun = details[6]

    denda = hitung_denda(tanggal_pinjam, tanggal_kembali)

    print(f"Denda keterlambatan: Rp{denda}")

    kembali[id_pinjam] = [nama, no, tanggal_pinjam, nama_buku, tanggal_kembali, denda]

    perpustakaan[id_buku] = [nama_buku, penulis, tahun]

    del pinjam[id_pinjam]

    print("Pengembalian berhasil dicatat.")


def data_kembali():
    if not kembali:
        print("Tidak ada Pengembalian.")
    else:
        print("Daftar Pengembalian:")
        for id, details in kembali.items():
            print(f"ID: {id}, Nama Peminjam: {details[0]}, No.Telepon: {details[1]}, "
                  f"Tanggal Pinjam: {details[2]}, Tanggal Kembali: {details[4]}, "
                  f"Buku: {details[3]}, Denda: Rp{details[5]}")


# =================== LOOP MENU ================================ #

while True:
    role = input("Apakah Anda admin atau user? (admin/user): ").strip().lower()
    if role == 'user':
        is_admin = False
        break
    elif role == 'admin':
        pw = input("Masukkan password: ").strip()
        if pw == 'admin123':  
            is_admin = True
            break
        else:
            print("Password salah. Coba lagi.")
    else:
        print("Pilihan tidak valid. Silakan pilih admin atau user.")

while True:
    if is_admin:
        menu_admin()
        pilih = input("Pilih opsi (1-10): ").strip()
        
        if pilih == '1':
            tampilkan()
        elif pilih == '2':
            cari()
        elif pilih == '3':
            tambah()
        elif pilih == '4':
            update()
        elif pilih == '5':
            hapus()
        elif pilih == '6':
            tambah_pinjam()
        elif pilih == '7':
            data_pinjam()
        elif pilih == '8':
            tambah_kembali()
        elif pilih == '9':
            data_kembali()
        elif pilih == '10':
            print("Terima kasih telah menggunakan Program Perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        menu_user()
        pilih = input("Pilih opsi (1-3): ").strip()
        
        if pilih == '1':
            tampilkan()
        elif pilih == '2':
            cari()
        elif pilih == '3':
            print("Terima kasih telah menggunakan Program Perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
