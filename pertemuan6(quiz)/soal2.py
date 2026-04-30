stok_gadget = [ 
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
]

batas_atas = int(input('masukkan batas atas:'))
batas_bawah = int(input('masukkan batas bawah:'))

def filter_harga(data, min_harga, max_harga):
    for i in range(len(stok_gadget)):
        if stok_gadget[i] > min_harga:
            if stok_gadget[i] < max_harga:
                return stok_gadget[i]


max_harga = int(input('masukkan max_harga:'))
min_harga = int(input('masukkan min_harga:'))
daftar = stok_gadget ( min_harga, max_harga)