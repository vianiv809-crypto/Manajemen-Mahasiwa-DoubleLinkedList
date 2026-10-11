class Node:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_urut(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        # Jika list kosong
        if self.head is None:
            self.head = new_node
            return
        
        # Jika NIM lebih kecil dari head, jadi head baru
        if nim < self.head.nim:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # Cari posisi yang pas
        current = self.head
        while current.next and current.next.nim < nim:
            current = current.next
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def tampil(self):
        if self.head is None:
            print("Data kosong")
            return
        current = self.head
        print("\n=== Daftar Mahasiswa ===")
        while current:
            print(f"NIM: {current.nim} | Nama: {current.nama} | Jurusan: {current.jurusan}")
            current = current.next

    def cari_di_array(self, nim):
        current = self.head
        while current:
            if current.nim == nim:
                print(f"Ditemukan: {current.nim} - {current.nama} - {current.jurusan}")
                return current
            current = current.next
        print(f"NIM {nim} tidak ada di ARRAY")
        return None

# === PROGRAM UTAMA ===
if __name__ == "__main__":
    dll = DoubleLinkedList()

    # Contoh input
    dll.tambah_urut(2301, "viani", "Teknik Informatika")
    dll.tambah_urut(2305, "gisel", "Sistem Informasi")
    dll.tambah_urut(2303, "Marci", "Teknik Informatika")

    dll.tampil()
    
    # Contoh cari
    dll.cari_di_array(2305)
    dll.cari_di_array(2303)