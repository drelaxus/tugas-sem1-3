class Node:
    def __init__(self, sku, product_name, stock):
        self.sku = sku
        self.product_name = product_name
        self.stock = stock
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, sku, product_name, stock):
        if self.root is None:
            self.root = Node(sku, product_name, stock)
        else:
            self._insert(self.root, sku, product_name, stock)

    def _insert(self, current_node, sku, product_name, stock):
        if sku < current_node.sku:
            if current_node.left is None:
                current_node.left = Node(sku, product_name, stock)
            else:
                self._insert(current_node.left, sku, product_name, stock)
        elif sku > current_node.sku:
            if current_node.right is None:
                current_node.right = Node(sku, product_name, stock)
            else:
                self._insert(current_node.right, sku, product_name, stock)
        else:
            print(f"SKU {sku} telah ada di dalam sistem.")

    def find(self, sku):
        return self._find(self.root, sku)

    def _find(self, current_node, sku):
        if current_node is None:
            return None
        elif sku == current_node.sku:
            return current_node
        elif sku < current_node.sku:
            return self._find(current_node.left, sku)
        else:
            return self._find(current_node.right, sku)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node)
            self._inorder(node.right, result)


class Transaction:
    def __init__(self, transaction_id, sku, quantity, subtotal):
        self.transaction_id = transaction_id
        self.sku = sku
        self.quantity = quantity
        self.subtotal = subtotal


class SITORSI:
    def __init__(self):
        self.bst = BST()
        self.transactions = []
        self.transaction_id = 0

    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("||\tSelamat Datang di Sistem Informasi\t||")
            print("||\t\tStok dan Transaksi\t\t||")
            print("=" * 50)
            print("=" * 19 + " MENU UTAMA " + "=" * 19)
            print("|| 0. Keluar Program \t\t\t\t||")
            print("|| 1. Kelola Stok Barang \t\t\t||")
            print("|| 2. Input Data Stok Barang \t\t\t||")
            print("|| 3. Restok Barang \t\t\t\t||")
            print("|| 4. Kelola Transaksi Konsumen \t\t||")
            print("=" * 50)

            pilihan = input("\nPilih Menu : ")

            if pilihan == "0":
                print("Terima Kasih.")
                break
            elif pilihan == "1":
                self.kelola_stok_barang()
            elif pilihan == "2":
                self.input_data_stok_barang()
            elif pilihan == "3":
                self.restok_barang()
            elif pilihan == "4":
                self.kelola_transaksi_konsumen()
            else:
                print("Pilihan tidak valid.")

    def kelola_stok_barang(self):
        print("\n" + "=" * 50)
        print("=" * 16 + " Data Stok Barang " + "=" * 16)
        stok_barang = self.bst.inorder()
        if not stok_barang:
            print("|| Masih Belum ada barang yang ditambahkan")
        else:
            for node in stok_barang:
                print(f"|| SKU: {node.sku}, Nama Produk: {node.product_name}, Stok: {node.stock}")

    def input_data_stok_barang(self):
        sku = input("Masukkan SKU: ")
        if self.bst.find(sku):
            print("SKU sudah ada di sistem.")
        else:
            product_name = input("Masukkan Nama Produk: ")
            stock = int(input("Masukkan Jumlah Stok: "))
            self.bst.insert(sku, product_name, stock)
            print("Data stok barang berhasil ditambahkan.")

    def restok_barang(self):
        sku = input("Masukkan SKU: ")
        node = self.bst.find(sku)
        if node:
            additional_stock = int(input("Masukkan Jumlah Restok: "))
            node.stock += additional_stock
            print("Stok berhasil diperbarui.")
        else:
            print("SKU tidak ditemukan.")

    def kelola_transaksi_konsumen(self):
        while True:
            print("\n" + "=" * 50)
            print("=" * 11 + " Kelola Transaksi Konsumen " + "=" * 11 + "=")
            print("|| 0. Kembali ke Menu Utama \t\t\t||")
            print("|| 1. Input Data Transaksi Baru \t\t||")
            print("|| 2. Lihat Data Seluruh Transaksi Konsumen \t||")
            print("|| 3. Lihat Data Transaksi Berdasarkan Subtotal ||")
            print("=" * 50)

            pilihan = input("\nPilih Menu : ")

            if pilihan == "0":
                break
            elif pilihan == "1":
                self.input_data_transaksi_baru()
            elif pilihan == "2":
                self.lihat_data_seluruh_transaksi()
            elif pilihan == "3":
                self.lihat_data_transaksi_berdasarkan_subtotal()
            else:
                print("Pilihan tidak valid.")

    def input_data_transaksi_baru(self):
        sku = input("Masukkan SKU: ")
        node = self.bst.find(sku)
        if not node:
            print("SKU tidak ditemukan.")
        else:
            quantity = int(input("Masukkan Jumlah Barang yang Dibeli: "))
            if quantity > node.stock:
                print("Jumlah stok tidak mencukupi.")
            else:
                subtotal = float(input("Masukkan Subtotal Transaksi: "))
                self.transaction_id += 1
                transaction = Transaction(self.transaction_id, sku, quantity, subtotal)
                self.transactions.append(transaction)
                node.stock -= quantity
                print("Transaksi berhasil ditambahkan.")

    def lihat_data_seluruh_transaksi(self):
        if not self.transactions:
            print("Tidak ada transaksi yang ditemukan.")
        else:
            for t in self.transactions:
                print(f"ID Transaksi: {t.transaction_id}, SKU: {t.sku}, Jumlah: {t.quantity}, Subtotal: {t.subtotal}")

    def lihat_data_transaksi_berdasarkan_subtotal(self):
        if not self.transactions:
            print("Tidak ada transaksi yang ditemukan.")
        else:
            subtotal_min = float(input("Masukkan Subtotal Minimum: "))
            subtotal_max = float(input("Masukkan Subtotal Maksimum: "))
            filtered_transactions = [t for t in self.transactions if subtotal_min <= t.subtotal <= subtotal_max]
            if not filtered_transactions:
                print("Tidak ada transaksi yang sesuai dengan kriteria.")
            else:
                for t in filtered_transactions:
                    print(f"ID Transaksi: {t.transaction_id}, SKU: {t.sku}, Jumlah: {t.quantity}, Subtotal: {t.subtotal}")


# Membuat instance SITORSI dan menjalankan menu
sitorsi = SITORSI()
sitorsi.menu()
