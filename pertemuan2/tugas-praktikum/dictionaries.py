#Dictionaries
#A. Dictionaries python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#digunakan untuk menyimpan nilai data dalam pasangan key:items
#Dictionaries adalah kumpulan yang terurut, dapat diubah, dan tidak mengizinkan duplikat.

#-Item:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#-Panjang dictionaries: Gunakan len()
print(len(thisdict))
#-Tipe data: Nilai dalam item dictionaries dapat berupa tipe data apa pun:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#Kita juga bisa menggunakan konstruktor dict() untuk membuat dictionaries.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#B. Access dictionaries items
#-Mengakses item
#Anda dapat mengakses item-item dalam dictionaries dengan merujuk pada nama key nya, yang berada di dalam tanda kurung siku:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

x = thisdict.get("model")#atau menggunakan get()
#-Key
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

x = thisdict.keys()#daftar key

#-Value
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

x = thisdict.values()#daftar nilai
#-Item
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

x = thisdict.items()
#Untuk menentukan apakah kunci tertentu ada dalam kamus, gunakan kata in kunci:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#C. Change dictionaries items:

#-Ubah nilai:Anda dapat mengubah nilai item tertentu dengan merujuk pada nama kuncinya:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#-Update dictionaries:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#D. Add dictionaries items:

#-Menambahkan items:dilakukan dengan menggunakan kunci indeks baru dan menetapkan nilai padanya
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Tambahkan item warna ke dictionaries dengan menggunakan update() metode:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#E. Remove dictionaries items:
#-Menghapus item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)#metode pop

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)#metode del

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)#metode clear: mengosongkan dictionaries

#F. Loop dictionaries

#Menggunakan for
#Cetak semua nama kunci dalam kamus, satu per satu:
for x in thisdict:
  print(x)
  
#Cetak semua nilai dalam kamus, satu per satu:
for x in thisdict:
  print(thisdict[x])
  
#Anda juga dapat menggunakan values()metode ini untuk mengembalikan nilai-nilai dari sebuah kamus:
for x in thisdict.values():
  print(x)
  
#Anda dapat menggunakan keys()metode ini untuk mengembalikan kunci-kunci dari sebuah kamus:
for x in thisdict.keys():
  print(x)
  
#Lakukan perulangan melalui kunci dan nilai , dengan menggunakan items()metode:
for x, y in thisdict.items():
  print(x, y)  

#G. Copy dictionaries

#Anda tidak dapat menyalin kamus hanya dengan mengetik dict2 = dict1, karena: dict2 hanya akan menjadi referensi ke dict1,
#dan perubahan yang dilakukan di dict1 akan secara otomatis juga dilakukan di dict2

#Menggunakan Copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Menggunakan dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#H. Nested dictionaries
#Sebuah kamus dapat berisi kamus-kamus lain, ini disebut kamus bersarang (nested dictionary).
 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} # kamus yang berisi 3 kamus

#-Mengakses item
print(myfamily["child2"]["name"])

#-Loop
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])