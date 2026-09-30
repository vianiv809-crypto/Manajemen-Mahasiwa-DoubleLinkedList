from linked_list import DoubleLinkedList

dll = DoubleLinkedList()

while True:
    print("\n=== PROGRAM MANAJEMEN DATA MAHASISWA ===")
    print("1. Tambah di Awal")
    print("2. Tambah di Akhir")
    print("3. Tambah Urut NIM (Tengah)")
    print("4. Hapus Data by NIM")
    print("5. Cari Data by NIM")
    print("6. Tampilkan Semua Data")
    print("0. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == '1' or pilih == '2' or pilih == '3':
        nim = int(input("Masukkan NIM (angka): "))
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        if pilih == '1': dll.tambah_awal(nim, nama, jurusan)
        if pilih == '2': dll.tambah_akhir(nim, nama, jurusan)
        if pilih == '3': dll.tambah_urut_nim(nim, nama, jurusan)
    elif pilih == '4':
        nim = int(input("NIM yang dihapus: "))
        dll.hapus_nim(nim)
    elif pilih == '5':
        nim = int(input("NIM yang dicari: "))
        h = dll.cari_nim(nim)
        if h: print(f"DITEMUKAN: {h.nim} - {h.nama} - {h.jurusan}")
        else: print("Tidak ditemukan")
    elif pilih == '6':
        dll.tampilkan()
    elif pilih == '0':
        break