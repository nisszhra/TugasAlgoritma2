import homework as hw

print(f'{5*"="}Selamat Datang Di Program Manajemen Barang{5*"="}')
print("Masukkan Pilihan")
print("1. Tambah Barang")
print("2. Cari Barang")
print("3. Hapus Barang")
print("4. Edit Barang")
print("5. Tampilkan Data Barang")
print("6. Tampilkan Jumlah Data")
print("7. Keluar")

while True:
    pilihan = int(input('Masukkan Pilihan: '))
    if pilihan == 1:
        hw.sum()
    elif pilihan == 2:
        hw.search()
    elif pilihan == 3:
        hw.delete()
    elif pilihan == 4:
        hw.edit()
    elif pilihan == 5:
        print(f"{10*'='}Toko Klontong{10*'='}")
        hw.view_data()
    elif pilihan == 6:
        hw.view_item_cout()
    elif pilihan == 7:
        print("Terima Kasih Telah Menggunakan Program Kami")
        break
