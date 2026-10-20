# Simulasi Risiko Banjir di Wilayah Bengkulu

## Deskripsi
Program Python sederhana untuk mengklasifikasikan risiko banjir berdasarkan input curah hujan (mm) dan tinggi air (cm). Proyek ini terinspirasi materi kuliah praktisi tentang *Bridging Global Infrastructure to Address Local Challenges in High Performance Computing (HPC)*, terutama contoh pemanfaatan komputasi untuk prediksi banjir dan kebutuhan lokal.

## Tujuan
- Menunjukkan bagaimana data lokal dapat diproses menggunakan program.
- Menggunakan aturan sederhana untuk menghasilkan kategori risiko.
- Menjadi proyek awal yang dapat dikembangkan menuju analisis data, simulasi, atau komputasi berskala lebih besar.

## Teknologi
- Python 3
- Terminal / command line
- CSV sebagai contoh data simulasi

Tidak memerlukan library tambahan.

## Cara menjalankan
1. Pastikan Python 3 telah terpasang.
2. Buka folder proyek di VS Code.
3. Buka terminal VS Code.
4. Jalankan:

```bash
python main.py
```

Jika perintah `python` tidak tersedia di Windows, coba:

```bash
py main.py
```

## Contoh input
- Nama wilayah: Muara Bangkahulu
- Curah hujan: 65
- Tinggi air: 90

## Aturan simulasi
- **TINGGI** jika curah hujan >= 100 mm atau tinggi air >= 150 cm.
- **SEDANG** jika curah hujan >= 50 mm atau tinggi air >= 80 cm.
- **RENDAH** jika tidak memenuhi aturan di atas.

Ambang tersebut hanya contoh untuk demonstrasi pemrograman, bukan standar resmi atau model prediksi ilmiah.

## Batasan
- Data tidak diambil langsung dari sensor atau sumber resmi.
- Program menggunakan aturan sederhana, bukan machine learning.
- Program tidak menjalankan komputasi pada supercomputer/HPC.
- Jangan gunakan hasil program sebagai peringatan banjir nyata.

## Pengembangan berikutnya
1. Menggunakan data historis resmi dan membersihkan datanya.
2. Mengevaluasi ambang risiko bersama ahli/instansi terkait.
3. Menambahkan visualisasi grafik.
4. Menguji model dengan data historis yang dipisahkan dari data pelatihan.
5. Jika kebutuhan komputasi benar-benar besar, mempelajari pemrosesan paralel dan lingkungan HPC.

## Kaitan dengan materi pemateri
Materi pemateri menekankan alur kerja dari masalah lokal, data, pemodelan/komputasi, hingga hasil yang dapat digunakan. Proyek ini memperagakan alur tersebut dalam skala kecil. Ini adalah implementasi pembelajaran yang terinspirasi materi, bukan implementasi HPC sesungguhnya.
