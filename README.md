# Data scraper API untuk website COVID-19 Kota Semarang

Bahasa Indonesia | [English](https://github.com/fmmochtar/covid-scrap-smg-api/blob/master/README_EN.md)

## Deskripsi
Aplikasi web scraper API ini digunakan untuk mengambil data COVID-19 dari web [COVID-19 Kota Semarang](https://siagacorona.semarangkota.go.id/halaman/odppdpv2) yang menampilkan jumlah kasus COVID-19 di wilayah Kota Semarang. Data yang diambil dari website tersebut selanjutnya diolah dan diteruskan menjadi data yang dapat digunakan oleh situs web lainnya menggunakan web API ini.

Aplikasi ini ditulis dengan bahasa pemrograman Python, menggunakan **FastAPI** sebagai back-end untuk layanan API, dan **uvicorn** sebagai ASGI.

## Persyaratan
- Python 3
- Package yang dibutuhkan (daftar ada di requirements.txt)

## Instalasi dan penggunaan awal
1. Install package yang terdapat pada requirements.txt dengan perintah berikut.
```
pip3 install -r requirements.txt
```
2. Jalankan dengan eksekusi langsung (dengan catatan sudah ada permission eksekusi, bila belum lakukan chmod +x pada run.py), atau dengan mengetikkan ```python3 ./run.py```.

## Konfigurasi

Konfigurasi dasar untuk menjalankan service dapat diatur menggunakan file `.env`. Bisa salin file `.env.example` lalu ubah namanya menjadi `.env` 
Berikut adalah konfigurasi secara default.

```
host_ip = '0.0.0.0'
host_port = '8000'

duration = 5
```
Keterangan:
```host_ip```: Alamat IP dari server / host.
```host_port```: Port layanan yang ingin digunakan.
```duration```: Waktu selang untuk restart layanan berkala (dalam menit).

Catatan: untuk melakukan expose service ini, pastikan nilai dari ```host_ip``` adalah ```0.0.0.0```.

## API Endpoint

Untuk melihat endpoint yang terdapat pada aplikasi API ini, dapat mengakses pada ```http://localhost:8000/docs```.

## Batasan
BeautifulSoup4 tidak memiliki kapabilitas untuk melakukan pengambilan data dan parse ulang setiap kali ada perubahan. Untuk menyajikan data secara mendekati real time dari situs web tanpa memberikan banyak HTTP request dalam jumlah banyak, saya memberikan fitur untuk restart layanan dalam hitungan menit.
