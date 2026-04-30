class NodeCLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None 

    def tambah_petugas(self, nama):
        new_node = NodeCLL(nama)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head 
            self.current = self.head  
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head 

    def giliran_berikutnya(self, n):
        if not self.head:
            print("Tidak ada petugas dalam daftar.")
            return

        for i in range(1, n + 1):
            print(f"Giliran {i}: {self.current.data}")
            self.current = self.current.next 


#PENGUJIAN SOAL 3: Rotasi Melingkar

print("= Output Soal 3: Giliran Valet =")
valet = CircularLinkedList()
valet.tambah_petugas("Andi")
valet.tambah_petugas("Budi")
valet.tambah_petugas("Citra")
valet.tambah_petugas("Dewi")

valet.giliran_berikutnya(6)
