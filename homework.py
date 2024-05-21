list_barang = {}

def sum():
    nama = input('Masukkan Nama Barang: ')
    if nama in list_barang:
        list_barang[nama] += 1
        print(f'Barang {nama} telah ditambahkan')
        return
    
    stok = int(input('Masukkan Jumlah Barang: '))
    list_barang[nama] = stok
    print(f'Barang : "{nama}" telah ditambahkan')
    print(f'Stok: {stok}')

def search():
    lihat = input('Cari Barang: ')
    if lihat in list_barang:
        print(f'{10*'='}Hasil Pencarian{10*'='}')
        print(f'Barang {lihat} tersedia {list_barang[lihat]} pcs')
    else:
        print(f'Barang {lihat} tidak tersedia')

def delete():
    hapus = input('Hapus Barang: ')
    if hapus in list_barang:
        del list_barang[hapus]
        print(f'Barang {hapus} telah dihapus')
    else:
        print(f'Barang {hapus} tidak tersedia')

def edit():
    nama = input('Masukkan barang yang ingin diubah: ')
    if nama in list_barang:
        stok = int(input('Masukkan jumlah barang: '))
        list_barang[nama] = stok
        print(f'Barang {nama} telah diubah')
    else:
        print(f'Barang {nama} tidak tersedia')

def view_data():
    print(f"{list_barang}")
    
def view_item_cout():
    if not list_barang:
        print('Tidak ada data')
        return
    print(f"Jumlah Data Barang Saat Ini :{len(list_barang)} barang")