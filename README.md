## SISTEM PEMESANAN MAKANAN SEDERHANA


### Disusun oleh:  

| Nama | NIM |
|--------|------|
| Deri | 2310511013 |
| Moh. Alfariz | 2310511017 |
| Ludy Haryanto | 2310511019 |


## 1. Pendahuluan

### 1.1 Tujuan
Dokumen ini menjelaskan kebutuhan fungsional dan non-fungsional dari aplikasi **Sistem Pemesanan Makanan Sederhana** berbasis Python CLI. Aplikasi ini dikembangkan sebagai simulasi proses pemesanan makanan.

### 1.2 Lingkup
Sistem ini memungkinkan pengguna untuk:
- Menampilkan daftar menu makanan dan harga
- Memesan makanan berdasarkan kode dan jumlah
- Melihat daftar pesanan
- Melihat total pembayaran

### 1.3 Definisi, Akronim, dan Singkatan

| Istilah | Arti |
|--------|------|
| CLI | Command Line Interface |
| SRS | Software Requirements Specification |
| User | Pengguna akhir aplikasi |
| Admin | Pemilik/pengelola sistem |


## 2. Deskripsi Umum

### 2.1 Perspektif Produk
Sistem standalone berbasis Python CLI, tidak memerlukan koneksi internet atau database eksternal.

### 2.2 Fungsi Sistem
- Menampilkan menu makanan
- Menambahkan pesanan
- Menampilkan struk pemesanan
- Menghitung total harga

### 2.3 Karakteristik Pengguna
Pengguna adalah pelanggan atau kasir. Tidak memerlukan keahlian teknis.


## 3. Kebutuhan Fungsional

| Kode | Nama Fitur | Deskripsi |
|------|------------|-----------|
| RF001 | Tampilkan Menu | Sistem menampilkan daftar makanan. |
| RF002 | Tambah Pesanan | Pengguna memilih makanan berdasarkan kode. |
| RF003 | Tampilkan Struk | Sistem menampilkan total dan daftar pesanan. |


## 4. Kebutuhan Non-Fungsional

| Kode | Deskripsi |
|------|-----------|
| RNF001 | Respon input < 1 detik |
| RNF002 | Berjalan pada Python 3.x |
| RNF003 | Antarmuka berbasis teks sederhana |


## 5. Antarmuka Sistem

### 5.1 Antarmuka Pengguna
- Terminal CLI berbasis teks

### 5.2 Antarmuka Perangkat Keras
- Komputer dengan Python 3.x

### 5.3 Antarmuka Perangkat Lunak
- Interpreter Python
- Tidak memerlukan library eksternal


## 6. Batasan Sistem

- Tidak menyimpan data
- Tidak mendukung login atau multi-user
- Tidak berbasis GUI

## 7. Lampiran

- Struktur file:
  - `menu.py`, `order.py`, `main.py`
- Alur sistem:

- Screenshot Hasil Running:
  
