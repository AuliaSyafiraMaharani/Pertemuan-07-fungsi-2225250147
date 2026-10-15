# Pertemuan 07 Fungsi Python
Nama: Aulia Syafira Maharani
NIM: 2225250147
Kelas: 3A

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular[cite: 11].

## Cara Menjalankan
python3 praktik/utilitas_matematika.py[cite: 11]

## Struktur Fungsi
* `luas_persegi_panjang(p, l)`: Menghitung luas persegi panjang berdasarkan parameter panjang dan lebar[cite: 6].
* `luas_segitiga(a, t)`: Menghitung luas segitiga berdasarkan alas dan tinggi[cite: 6].
* `jumlah_n(n)`: Menghitung total penjumlahan angka dari 1 sampai n.
* `faktorial(n)`: Menghitung nilai faktorial dari bilangan bulat nonnegatif.

## Hasil Pengujian
| Fungsi | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| luas_persegi_panjang | p=8, l=5 | 40 | 40 | Lulus[cite: 11] |
| luas_segitiga | a=10, t=6 | 30.0 | 30.0 | Lulus[cite: 11] |
| jumlah_n | n=10 | 55 | 55 | Lulus[cite: 11] |
| faktorial | n=5 | 120 | 120 | Lulus[cite: 11] |

## Refleksi
Program menjadi jauh lebih terstruktur dan mudah diuji karena rumus matematika dipisahkan ke dalam fungsi-fungsi mandiri yang dapat dipanggil kembali tanpa harus menulis ulang kode berulang kali[cite: 5, 8].