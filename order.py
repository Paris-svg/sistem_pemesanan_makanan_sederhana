from menu import menu_items

class Order:
    def __init__(self):
        self.pesanan = []

    def tambah_pesanan(self, kode_menu, jumlah):
        if kode_menu in menu_items:
            item = menu_items[kode_menu]
            total_harga = item["harga"] * jumlah
            self.pesanan.append({
                "nama": item["nama"],
                "jumlah": jumlah,
                "harga_satuan": item["harga"],
                "total": total_harga
            })
            print(f"{jumlah} x {item['nama']} berhasil ditambahkan.")
        else:
            print("Kode menu tidak valid.")

    def tampilkan_struk(self):
        print("\n=== STRUK PEMBELIAN ===")
        total_bayar = 0
        for item in self.pesanan:
            print(f"{item['jumlah']} x {item['nama']} = Rp{item['total']}")
            total_bayar += item["total"]
        print(f"Total Bayar: Rp{total_bayar}")
