# iPBB NOP Detail Finder (Kab Tangerang)

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Skrip Python untuk mencari detail dari Nomor Objek Pajak (NOP), termasuk alamat, RT/RW, luas bumi, luas bangunan, dan detil pajak untuk setiap tahunnya.

## Overview

Repository ini berisi skrip Python (`nop_detail_finder.py`) yang mengambil informasi detail properti berdasarkan NOP yang diberikan. Skrip ini menggunakan teknik web scraping untuk mengekstrak informasi dari sumber resmi di mana detail NOP tersedia secara publik.

## Fitur

- **Cari berdasarkan NOP**: Masukkan NOP yang valid dan dapatkan informasi detail properti.
- **Beberapa Tahun**: Ambil detail pajak untuk setiap tahun yang tersedia.
- **Parsing Data**: Ekstrak detail spesifik seperti alamat, RT/RW, luas bumi, luas bangunan, dan jumlah pajak.

## Persyaratan

- Python 3.x
- Dependensi/Modul 'requests' untuk python

## Penggunaan
1. Clone repository ini:
2. Instal dependensi:
3. Jalankan skrip dengan NOP sebagai argumen ATAU ubah variabel `USE_ARGUMENT` dan `NOP` di dalam skrip:
Replace `<NOP>` with the actual Nomor Objek Pajak you want to search for.
4. Skrip akan mengambil dan menampilkan detail properti termasuk alamat, RT/RW, luas bumi, luas bangunan, dan detil pajak untuk setiap tahun yang tersedia.


## Contoh

```bash
python nop_detail_finder.py 361901234567890123
```
