def tambah_kontak():
    nama = input("Nama: ")
    telp = input("No Telepon: ")
    kontak[nama] = telp
    print("Kontak berhasil ditambahkan")


def tampilkan_kontak():
    print("Daftar kontak:")
    for k, v in kontak.items():
        print("Nama: {} \nNo Telepon: {}".format(k, v))


def hapus_kontak():
    nama = input("Nama kontak yang ingin dihapus: ")
    kontak.pop(nama)
    print("Kontak berhasil dihapus")


def edit_kontak():
    nama = input("Nama kontak yang ingin diubah: ")
    telp = input("No Telepon: ")
    edit = {nama: telp}
    kontak.update(edit)
    print("Kontak berhasil diubah")


def panggil_menu(menu):
    if menu == '1':
        tampilkan_kontak()
    elif menu == '2':
        tambah_kontak()
    elif menu == '2a':
        hapus_kontak()
    elif menu == '2b':
        edit_kontak()
    else:
        print("Menu tidak tersedia")


print("Selamat Datang!")
print("\n--- Menu ---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")
kontak = {}
menu = input("\nPilih menu: ")
while (menu != '3'):
    panggil_menu(menu)
    menu = input("\nPilih menu: ")

print("Program selesai, sampai jumpa!")