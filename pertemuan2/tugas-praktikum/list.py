#List digunakan untuk menyimpan banyak item dalam satu variabel.
#contoh:
thislist = ["apple", "banana", "cherry"]
print(thislist)
#Item dalam daftar diurutkan, dapat diubah, dan memungkinkan nilai duplikat.

#-Panjang daftar:
#Untuk menentukan berapa banyak item yang dimiliki sebuah daftar, gunakan len()fungsi berikut:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#Item dalam daftar dapat berupa tipe data apa pun:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#B.access list items:

#Item dalam daftar diindeks dan Anda dapat mengaksesnya dengan merujuk pada nomor indeks:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#-Pengindeksan Negatif:Pengindeksan negatif berarti mulai dari akhir.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#-Rentang Indeks
#Anda dapat menentukan rentang indeks dengan menentukan di mana rentang tersebut dimulai dan di mana rentang tersebut berakhir.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#-Check
#Untuk menentukan apakah suatu item tertentu ada dalam sebuah daftar, gunakan in kata kunci:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#C. Change list items:

#-Ubah Nilai Item: Untuk mengubah nilai item tertentu, lihat nomor indeksnya:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#-Rentang Nilai Item
#Untuk mengubah nilai item dalam rentang tertentu, definisikan daftar dengan nilai baru, 
#dan rujuk ke rentang nomor indeks tempat Anda ingin memasukkan nilai baru:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#-Sisipkan Item
#Untuk menyisipkan item daftar baru, tanpa mengganti nilai yang sudah ada, kita dapat menggunakan insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#D. Add list items:

#-Tambahkan Item:Untuk menambahkan item ke akhir daftar, gunakan append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#-Sisipkan Item
#Untuk menyisipkan item daftar pada indeks tertentu, gunakan insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#-Perluas Daftar
#Untuk menambahkan elemen dari daftar lain ke daftar saat ini, gunakan extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#E. Remove list items:

#-Hapus Item yang Ditentukan:Metode ini remove()menghapus item yang ditentukan.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Jika terdapat lebih dari satu item dengan nilai yang ditentukan, remove()metode ini akan menghapus item yang pertama muncul
#-Hapus Indeks yang Ditentukan:Metode ini pop()menghapus indeks yang ditentukan.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Jika Anda tidak menentukan indeks, pop()metode ini akan menghapus item terakhir.
#deljuga menghapus indeks yang ditentukan:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#deljuga dapat menghapus daftar sepenuhnya.
thislist = ["apple", "banana", "cherry"]
del thislist
#-Bersihkan Daftar
#Metode ini clear()mengosongkan daftar.Daftar itu masih ada, tetapi tidak berisi apa pun.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#F. Loop list:

#-Mengulang Melalui Daftar:
#Anda dapat mengulang melalui item daftar dengan menggunakan for perulangan:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#perulangan melalui nomor indeks.
#Anda juga dapat melakukan perulangan melalui item daftar dengan merujuk pada nomor indeksnya.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#-Menggunakan Loop While
#Anda dapat mengulang melalui item daftar dengan menggunakan whileperulangan.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#G. list comprehension

#-Pemahaman Daftar:
#List comprehension menawarkan sintaks yang lebih singkat ketika Anda ingin membuat daftar baru 
#berdasarkan nilai-nilai dari daftar yang sudah ada.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#-Sintaks
#kondisi:filter yang hanya menerima item yang dievaluasi menjadi True.
newlist = [x for x in fruits if x != "apple"]
#dapat diulang:
newlist = [x for x in range(10)]
#ekspresi:item saat ini dalam iterasi, tetapi juga merupakan hasilnya, 
#yang dapat Anda manipulasi sebelum akhirnya menjadi item daftar dalam daftar baru
newlist = [x.upper() for x in fruits]

#H. Sort list

#-Urutkan Daftar Secara Alfanumerik:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#-Urutkan menurun:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#-Pengurutan Tidak Peka Huruf Besar/Kecil
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#-urutan terbalik
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#I. Copy list

#-Salin daftar
#copy:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#list:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#slice:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#J. Join list

#-gabungkan dua list
#Menggunakan +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#append
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
