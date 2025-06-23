class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self, capacity):
        self.top = None
        self.capacity = capacity
        self.size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.size == self.capacity

    def push(self, data):
        if self.is_full():
            print("Stack sudah penuh!")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack kosong, tidak bisa menghapus.")
            return
        removed_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Data {removed_data} telah dihapus dari stack.")

    def peek(self):
        if self.is_empty():
            print("Stack kosong.")
        else:
            print("Puncak Stack:", self.top.data)

    def get_size(self):
        print("Ukuran Stack saat ini:", self.size)

    def print_stack(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Stack:", elements[::-1])  # Tampilkan dari bawah ke atas

# Main Program
def main():
    kapasitas = 5
    stack = StackLinkedList(kapasitas)

    while True:
        print("\nPilih menu berikut ini :")
        print("1. Menambah isi stack")
        print("2. Menghapus isi stack")
        print("3. Cek Ukuran Stack saat ini")
        print("4. Cek Puncak Stack")
        print("5. Cek Stack Full")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan anda : ")

        if pilihan == '1':
            while not stack.is_full():
                isi = input("Masukkan isi stack : ")
                stack.push(isi)
                stack.print_stack()
                if stack.is_full():
                    print("Stack sudah penuh!")
                    break
                tambah = input("Menambah isi Stack Pilih [Ya/Tidak] : ").lower()
                if tambah != 'ya':
                    break
        elif pilihan == '2':
            stack.pop()
            stack.print_stack()
        elif pilihan == '3':
            stack.get_size()
        elif pilihan == '4':
            stack.peek()
        elif pilihan == '5':
            print("Stack penuh." if stack.is_full() else "Stack belum penuh.")
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
