class Transaction:
    def __init__(self):
        self.transactions = {}

    def add_item(self, detail):    
        nama_item = detail[0] 
        qty = detail[1] 
        harga = detail[2]

        if nama_item in self.transactions:
            self.transactions[nama_item][0] += qty
            self.transactions[nama_item][1] += harga
        else:
            self.transactions[nama_item] = [qty, harga]

    def delete_item(self, nama_item):
        if nama_item not in self.transactions:
            print("Item yang ingin dihapus tidak terdaftar")
        else:
            self.transactions.pop(nama_item)
            print("Data berhasil dihapus")

    def reset_transaction(self):
        list_name = []

        for nama_item in self.transactions.keys():
            list_name.append(nama_item)

        for x in list_name:
            self.transactions.pop(x)

        print("Semua item berhasil dihapus!")

    def total_price(self):
        total = 0

        for _, value in self.transactions.items():
            total += value[1]

        if total > 200000:
            total = total - (total * (5 / 100))
        elif total > 300000:
            total = total - (total * (8 / 100))
        elif total > 500000:
            total = total - (total * (10 / 100))
            
        print("Item yang dibeli adalah :", self.transactions)
        print("Total Belanja yang harus dibayarkan adalah Rp.", total)

    def update_item_qty(self, nama_item, jumlah_item):
        if nama_item not in self.transactions:
            print("Item yang ingin diubah tidak terdaftar")
        else:
            self.transactions[nama_item][0] = jumlah_item
            print("Data berhasil diupdate")
    
    def update_item_price(self, nama_item, harga):
        if nama_item not in self.transactions:
            print("Item yang ingin diubah tidak terdaftar")
        else:
            self.transactions[nama_item][1] = harga
            print("Data berhasil diupdate")
    
    def update_item_name(self, nama_item, update_nama_item):
        if nama_item not in self.transactions:
            print("Item yang ingin diubah tidak terdaftar")
        else:
            self.transactions[update_nama_item] = self.transactions[nama_item]
            self.transactions.pop(nama_item)
            print("Data berhasil diupdate")

    def check_order(self):
        i = 1
        print('| No | Nama Item | Jumlah Item | Harga / Item | Total Harga |') 

        for nama_item, value in self.transactions.items():
            print('|', i, '|', nama_item, '|', value[0], '|', value[1], '|', value[0] * value[1], '|') 
            i += 1
        
trnsct_123 = Transaction()
trnsct_123.add_item(['Ayam Goreng', 2, 100000])
trnsct_123.add_item(['Ikan Goreng', 5, 30000])
trnsct_123.add_item(['Ayam Goreng', 3, 150000])
print("Item yang dibeli adalah :", trnsct_123.transactions)

trnsct_123.check_order()

trnsct_123.delete_item('Ikan Goreng')
print("Sisa item :", trnsct_123.transactions)

trnsct_123.update_item_qty('Ayam Goreng', 2)
trnsct_123.update_item_price('Ayam Goreng', 5000)
trnsct_123.update_item_name('Ayam Goreng', 'Ayam Bakar')

trnsct_123.total_price()

trnsct_123.reset_transaction()
print("Item yang dibeli adalah :", trnsct_123.transactions)
