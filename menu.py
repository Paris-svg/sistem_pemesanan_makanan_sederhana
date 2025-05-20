menu_items = {
    "1": {"nama": "Nasi Goreng", "harga": 15000},
    "2": {"nama": "Mie Ayam", "harga": 12000},
    "3": {"nama": "Sate Ayam", "harga": 18000},
    "4": {"nama": "Es Teh", "harga": 5000}
}

def tampilkan_menu():
    print("=== MENU MAKANAN ===")
    for kode, item in menu_items.items():
        print(f"{kode}. {item['nama']} - Rp{item['harga']}")
