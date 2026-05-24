class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)

        return total % self.size

    def insert(self, kode, judul):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for data in bucket:
            if data[0] == kode:
                data[1] = judul
                print(f"Data {kode} berhasil diupdate")
                return

        bucket.append([kode, judul])
        print(f"Data {kode} berhasil ditambahkan")

    def search(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for data in bucket:
            if data[0] == kode:
                return data[1]

        return "Buku tidak ditemukan"

    def delete(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for i, data in enumerate(bucket):
            if data[0] == kode:
                del bucket[i]
                print(f"Data {kode} berhasil dihapus")
                return

        print("Buku tidak ditemukan")

    def display(self):
        print("\nISI HASH TABLE")
        print("=" * 40)

        for i, bucket in enumerate(self.table):
            print(f"Bucket {i} :", end=" ")

            if not bucket:
                print("Kosong")
            else:
                for data in bucket:
                    print(f"[{data[0]} : {data[1]}]", end=" ")
                print()

buku = HashTable()
print("=INSERT DATA AWAL=")
buku.insert("BK111", "Mahir C++ Dalam Satu Jam")
buku.insert("BK222", "Python Dasar")
buku.insert("BK333", "Matematika Diskrit")
buku.insert("BK444", "Atomic Habits")

print("\n=1=")
buku.display()

buku.insert("BK045", "Mein Kampf")
buku.insert("BK111", "Bumi Manusia")

print("\n=2=")
buku.display()

print("\nHASIL SEARCH")
print("BK222 :", buku.search("BK222"))
print("BK999 :", buku.search("BK999"))

print("\nDELETE DATA")
buku.delete("BK333")

print("\n=3=")
buku.display()