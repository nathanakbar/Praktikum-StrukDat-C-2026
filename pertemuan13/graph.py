class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)

        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

        print(f"[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)")

    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")

        for kota in self.graph:
            print(f"- {kota} terhubung ke:", end=" ")

            tetangga = []
            for tujuan, jarak in self.graph[kota]:
                tetangga.append(f"{tujuan} ({jarak})")

            print(", ".join(tetangga))

    def dijkstra(self, asal):
        jarak = {}
        dikunjungi = {}

        for kota in self.graph:
            jarak[kota] = float('inf')
            dikunjungi[kota] = False

        jarak[asal] = 0

        for _ in range(len(self.graph)):
            min_jarak = float('inf')
            kota_sekarang = None

            for kota in self.graph:
                if not dikunjungi[kota] and jarak[kota] < min_jarak:
                    min_jarak = jarak[kota]
                    kota_sekarang = kota

            if kota_sekarang is None:
                break

            dikunjungi[kota_sekarang] = True

            for tetangga, bobot in self.graph[kota_sekarang]:
                if not dikunjungi[tetangga]:
                    if jarak[kota_sekarang] + bobot < jarak[tetangga]:
                        jarak[tetangga] = jarak[kota_sekarang] + bobot

        return jarak

print('SISTEM NAVIGASI LOGISTIK "KILAT MAJU"')
print("=" * 40)

g = Graph()

g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)

g.tampilkan_graph()

print("\n[PROSES] Menghitung rute terpendek dari: Jakarta...")

hasil = g.dijkstra("Jakarta")

print("\n[HASIL] Jarak Terpendek dari Jakarta:")

no = 1
for kota, jarak in hasil.items():
    if kota != "Jakarta":
        print(f"{no}. Ke {kota}: {jarak} km")
        no += 1

print("=" * 40)
print("Simulasi Navigasi Selesai!")