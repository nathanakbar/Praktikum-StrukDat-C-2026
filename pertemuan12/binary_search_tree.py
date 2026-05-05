class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.counter = 1 

    def insert(self, id_buku, judul):
        if self.root is None:
            self.root = Node(id_buku, judul)
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        self._insert_recursive(self.root, id_buku, judul)

    def _insert_recursive(self, current_node, id_buku, judul):
        if id_buku < current_node.id_buku:
            if current_node.left is None:
                current_node.left = Node(id_buku, judul)
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self._insert_recursive(current_node.left, id_buku, judul)
        elif id_buku > current_node.id_buku:
            if current_node.right is None:
                current_node.right = Node(id_buku, judul)
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self._insert_recursive(current_node.right, id_buku, judul)
        else:
            print(f"[INSERT] ID {id_buku} sudah ada dalam sistem.")

    def search(self, id_buku):
        result = self._search_recursive(self.root, id_buku)
        if result is not None:
            print(f"[SEARCH] Mencari ID {id_buku}... Ditemukan! Judul: {result.judul}")
        else:
            print(f"[SEARCH] Mencari ID {id_buku}... Data tidak ditemukan.")

    def _search_recursive(self, current_node, id_buku):
        if current_node is None or current_node.id_buku == id_buku:
            return current_node
        
        if id_buku < current_node.id_buku:
            return self._search_recursive(current_node.left, id_buku)
        
        return self._search_recursive(current_node.right, id_buku)

    def traversal_inorder(self):
        print("[INFO] Koleksi Buku (In-Order Traversal):")
        self.counter = 1
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        if current_node is not None:
            self._inorder_recursive(current_node.left)
            print(f"{self.counter}. {current_node.id_buku} - {current_node.judul}")
            self.counter += 1
            self._inorder_recursive(current_node.right)

    def get_min(self):
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.id_buku

    def get_max(self):
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.id_buku

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, current_node):
        if current_node is None:
            return -1 
        
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)
        
        return max(left_height, right_height) + 1


print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=========================================")
    
katalog = BST()
    
katalog.insert(50, "Dasar Pemrograman")
katalog.insert(30, "Struktur Data")
katalog.insert(70, "Kecerdasan Buatan")
katalog.insert(20, "Matematika Diskrit")
katalog.insert(40, "Basis Data")
katalog.insert(60, "Jaringan Komputer")
katalog.insert(80, "Sistem Operasi")
print()
    
katalog.traversal_inorder()
print()
    
katalog.search(60)
katalog.search(100)
print()
    
print(f"[STATISTIK] ID Terkecil: {katalog.get_min()}")
print(f"[STATISTIK] ID Terbesar: {katalog.get_max()}")
print(f"[INFO] Tinggi (Height) Tree: {katalog.height()}")
print("=========================================")
print("Simulasi Selesai!")
