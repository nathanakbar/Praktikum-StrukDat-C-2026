#soal 1
pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False}, 
]

def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status")
    print("---------------------------------------------")
    
    for i, p in enumerate(pengunjung_hari_ini, 1):
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(f"{i}  | {p['id']} | {p['nama']} | {p['usia']}  | {p['kategori']} | {status}")

def filter_belum_kembali():
    belum = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    belum.sort()  
    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    for i, nama in enumerate(belum, 1):
        print(f"{i}. {nama}")
    print(f"Total belum kembali: {len(belum)} pengunjung")


tampilkan_pengunjung()
filter_belum_kembali()


#soal 2
info_perpustakaan = ('Nama : Perpustakaan Kampus Terpadu',
'Alamat  : Jl. Pendidikan No. 5, Pekanbaru',
'Telp    : 0761-54321')

rekap_kategori = set(info_perpustakaan)
print(f"Kategori Buku Unik : {rekap_kategori}")

jumlah_kategori = {}
for item in info_perpustakaan:
    if item in jumlah_kategori:
        jumlah_kategori[item] += 1
    else:
        jumlah_kategori[item] = 1
        
print(f"jumlah kategori: {jumlah_kategori}")

max_buku = max(jumlah_kategori.values())

buku_terlaris = [item for item, jumlah in jumlah_kategori.items() if jumlah == max_buku]

print(f"\nBuku paling laris ({max_buku} ):")
for barang in buku_terlaris:
    print(f"- {barang}")

#soal 3
class Pengunjung:
    pengunjung = 0
    
    def __init__(self,__id, __nama, __kategori):
        self.__id = id
        self.__nama = __nama
        self.__kategori = __kategori
    
    def get__id(self):
        return self.__id
    def get__nama(self):
        return self.__nama
    def get__kategori(self):
        return self.__kategori
#static method

#soal 1
print('''===== DATA PENGUNJUNG PERPUSTAKAAN ===== 
No | ID   | Nama   | Usia | Kategori | Status Kembali 
---+------+--------+------+----------+--------------- 
1  | M001 | Rina   | 20   | Fiksi    | Belum Kembali 
2  | M002 | Hendra | 23   | Sains    | Sudah Kembali 
3  | M003 | Siti   | 19   | Fiksi    | Belum Kembali 
4  | M004 | Taufik | 21   | Hukum    | Sudah Kembali 
5  | M005 | Yuni   | 18   | Sains    | Belum Kembali 
6  | M006 | Bagas  | 22   | Hukum    | Belum Kembali 
 
===== PENGUNJUNG BELUM KEMBALI ===== 
1. Bagas 
2. Rina 
3. Siti 
4. Yuni 
Total belum kembali: 4 pengunjung''')

#soal 2
print('''Info Perpustakaan: 
Nama    : Perpustakaan Kampus Terpadu 
Alamat  : Jl. Pendidikan No. 5, Pekanbaru 
Telp    : 0761-54321 
 
Kategori Buku Unik: {'Fiksi', 'Sains', 'Hukum'} 
Jumlah kategori: 3 
 
Rekap per kategori: 
Fiksi  : 2 pengunjung 
Sains  : 2 pengunjung 
Hukum  : 2 pengunjung 
 
Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung) ''')

#soal 3
print('''ID       : M001 
Nama     : Rina 
Kategori : Fiksi 
 
ID         : M007 
Nama       : Gilang 
Kategori   : Referensi 
Prioritas  : Mendesak 
** Layani segera! ** 
 
Total pengunjung terdaftar: 2''')

#soal 4
print('''===== ANTRIAN PEMINJAMAN ===== 
[1] M001 - Rina   | Fiksi 
[2] M002 - Hendra | Sains 
[3] M003 - Siti   | Fiksi 
[4] M004 - Taufik | Hukum 
Total antrian: 4 
 
Memanggil pengunjung berikutnya... 
Silakan masuk: Rina (M001) - Fiksi 
 
===== ANTRIAN PEMINJAMAN ===== 
[1] M002 - Hendra | Sains 
[2] M003 - Siti   | Fiksi 
[3] M004 - Taufik | Hukum 
Total antrian: 3 
 
Menghapus pengunjung dengan ID M003... 
Siti (M003) berhasil dihapus dari antrian. 
 
===== ANTRIAN PEMINJAMAN ===== 
[1] M002 - Hendra | Sains 
[2] M004 - Taufik | Hukum 
Total antrian: 2 
 
Mencari 'Taufik'... 
Ditemukan: M004 - Taufik | Hukum (posisi ke-2) 
 
Total antrian: 2''')
        

