from menu import tampilkan_menu
from order import Order

def main():
    pesanan = Order()

    while True:
        tampilkan_menu()
        kode = input("Masukkan kode menu (atau 'q' untuk selesai): ").strip()
        if kode.lower() == 'q':
            break
        jumlah = input("Masukkan jumlah: ").strip()
        if not jumlah.isdigit():
            print("Jumlah harus berupa angka!")
            continue
        pesanan.tambah_pesanan(kode, int(jumlah))

    pesanan.tampilkan_struk()

if __name__ == "__main__":
    main()
