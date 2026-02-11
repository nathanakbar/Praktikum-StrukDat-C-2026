#Tuple
#Tuple digunakan untuk menyimpan beberapa item dalam satu variabel.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#A. Item tuple:Item dalam tuple diurutkan, tidak dapat diubah, dan memungkinkan nilai duplikat.

#-Panjang Tuple
#Untuk menentukan berapa banyak item yang dimiliki sebuah tuple, gunakan len()
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#Item Tuple - Tipe Data
#Item dalam tuple dapat berupa tipe data apa pun:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#B. Access tuple items:
#Item dalam tuple diindeks dan Anda dapat mengaksesnya dengan merujuk pada nomor indeks:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#-Pengindeksan Negatif:Pengindeksan negatif berarti mulai dari akhir.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#-Rentang Indeks
#Anda dapat menentukan rentang indeks dengan menentukan di mana rentang tersebut dimulai dan di mana rentang tersebut berakhir.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#-Check
#Untuk menentukan apakah suatu item tertentu ada dalam sebuah tuple, gunakan in kata kunci:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
#C. Update Tuple

#-Mengubah nilai tuple:
# Anda dapat mengubah tuple menjadi list, mengubah list tersebut, dan mengubah list tersebut kembali menjadi tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#-Tambahkan item:konversi menjadi list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#Menambahkan tuple ke tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#-Hapus barang:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#D. Unpack tuple

#menguraikan tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#Menggunakan Asterisk
#Jika jumlah variabel kurang dari jumlah nilai, Anda dapat menambahkan awalan *pada nama variabel
#dan nilai-nilai tersebut akan diberikan ke variabel sebagai daftar:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#Jika tanda bintang ditambahkan ke nama variabel selain yang terakhir, 
#Python akan menetapkan nilai ke variabel tersebut hingga jumlah nilai yang tersisa sama dengan jumlah variabel yang tersisa.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#F. Loop tuple:

#-Mengulang Melalui tuple:
#Anda dapat mengulang melalui item tuple dengan menggunakan for perulangan:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#perulangan melalui nomor indeks.
#Anda juga dapat melakukan perulangan melalui item tuple dengan merujuk pada nomor indeksnya.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#-Menggunakan Loop While
#Anda dapat mengulang melalui item tuple dengan menggunakan whileperulangan.
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#J. Join tuple

#-gabungkan dua tuple: Menggunakan +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#Mengalikan tuple: Menggunakan *
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
