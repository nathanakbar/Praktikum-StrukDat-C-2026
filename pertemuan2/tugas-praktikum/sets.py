#Sets
#Himpunan (set) digunakan untuk menyimpan beberapa item dalam satu variabel.
#A. Set
#Himpunan adalah koleksi yang tidak terurut , tidak dapat diubah , dan tidak terindeks .
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplikat tidak diizinkan: Suatu himpunan tidak boleh memiliki dua item dengan nilai yang sama.
#Nilai True=1 dan False=0 (diabaikan salah satunya)
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#Menghtung panjang set: Menggunakan len()
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#Tipe data: Item dalam himpunan dapat berupa tipe data apa pun:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#Konstruktor set: Kita juga bisa menggunakan konstruktor set() untuk membuat himpunan.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#B. Access set items:
#-Akses item:
#Anda tidak dapat mengakses item dalam suatu himpunan dengan merujuk pada indeks atau kunci.
#Namun Anda dapat melakukan perulangan melalui item-item dalam himpunan menggunakan sebuah for loop, 
#atau menanyakan apakah nilai tertentu ada dalam himpunan, dengan menggunakan inkata kunci.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Periksa apakah "pisang" ada dalam himpunan tersebut
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#-Ubah items:
#Setelah sebuah set dibuat, Anda tidak dapat mengubah item di dalamnya, tetapi Anda dapat menambahkan item baru.

#C. Add set items:

#-Tambahkan items:
#Setelah sebuah set dibuat, Anda tidak dapat mengubah item di dalamnya, tetapi Anda dapat menambahkan item baru.
#Untuk menambahkan satu item ke dalam suatu set, gunakan add() metode ini.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#-Tambahkan set:
#Untuk menambahkan item dari set lain ke set saat ini, gunakan update() metode tersebut.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#-Tambahkan iterable apapun
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#D. Remove set items:
#-Hapus item: Untuk menghapus item dalam suatu set, gunakan metode remove(), atau discard().
#remove
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#discard
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#Hapus item secara acak dengan menggunakan pop() metode:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Metode clear() mengosongkan himpunan:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#Kata kunci del akan menghapus seluruh himpunan:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#E. Loop set:

#-Item loop:
#Anda dapat melakukan perulangan melalui item-item dalam himpunan dengan menggunakan for perulangan:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#F. Join set;

#-Union
#Metode ini union()mengembalikan himpunan baru yang berisi semua item dari kedua himpunan tersebut.
#menggunakan operator | dan union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#Gabungkan beberapa himpunan dengan union()metode:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#Gabungkan himpunan dengan tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#-Update
#Metode ini update()memasukkan item-item dalam set2 ke dalam set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#-Intersection
#Gabungkan set1 dan set2, tetapi hanya simpan yang duplikat
#Menggunakan operator & dan Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#-Difference
#Simpan semua item dari set1 yang tidak ada di set2:
#Menggunakan operator - dan Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#-symmetric_difference()
#simpan barang-barang yang tidak ada di kedua set:
#menggunakan operator ^ dan symmetric_difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#G. Frozen set

#frozenset adalah versi himpunan yang tidak dapat diubah.
#Seperti himpunan, ia berisi elemen-elemen unik, tidak berurutan, dan tidak dapat diubah.
#Tidak seperti himpunan, elemen tidak dapat ditambahkan atau dihapus dari frozenset.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
