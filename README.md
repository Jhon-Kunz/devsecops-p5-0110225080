# Kalkulator Sederhana (DevSecOps Pipeline)

**1. Deskripsi Aplikasi**
Aplikasi Python berbasis CLI untuk melakukan operasi matematika dasar dan validasi input untuk memastikan integritas data.

**2. Bahasa/Framework**
- Python 3.10+
- Pytest (untuk Unit Testing)

**3. Cara Menjalankan Aplikasi**
```bash
pip install -r requirements.txt
python main.py

**4. Overview Pipeline
Pipeline diimplementasikan menggunakan GitHub Actions yang terpicu saat ada push atau pull_request ke branch main. Pipeline terdiri dari dua tahap:

Build & Test: Menginstal dependencies dan menjalankan unit test dengan pytest.

SAST Scan: Menjalankan analisis keamanan kode statis menggunakan Bandit setelah tahap build berhasil.
