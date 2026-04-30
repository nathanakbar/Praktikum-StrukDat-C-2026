class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = NodeDLL(plat)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def tampilkan_mundur(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

    def hapus_kendaraan(self, plat):
        current = self.head
        
        while current:
            if current.data == plat:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None 
                
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            
            current = current.next


#PENGUJIAN SOAL 1: Penelusuran Maju & Mundur

print("= Output Soal 1: Parkir Dua Arah =")
parkir = DoubleLinkedList()
parkir.tambah_kendaraan("B 1234 ABC")
parkir.tambah_kendaraan("D 5678 XYZ")
parkir.tambah_kendaraan("A 9999 TUV")

print("[Maju]")
parkir.tampilkan_maju()

print("[Mundur]")
parkir.tampilkan_mundur()

#PENGUJIAN SOAL 2: Hapus Kendaraan dari Tengah

print("= Output Soal 2: Hapus Kendaraan =")
parkir_hapus = DoubleLinkedList()
parkir_hapus.tambah_kendaraan("B 1111 AA")
parkir_hapus.tambah_kendaraan("D 2222 BB")
parkir_hapus.tambah_kendaraan("A 3333 CC")
parkir_hapus.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
parkir_hapus.tampilkan_maju()

#Hapus kendaraan di tengah
parkir_hapus.hapus_kendaraan("A 3333 CC")

print("Sesudah:")
parkir_hapus.tampilkan_maju()
