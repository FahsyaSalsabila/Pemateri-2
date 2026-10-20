# Studi Kasus: Simulasi Prediksi Risiko Banjir di Wilayah Bengkulu

## 1. Latar Belakang

Banjir merupakan salah satu permasalahan lingkungan yang dapat mengganggu aktivitas masyarakat dan menyebabkan kerugian. Salah satu upaya untuk mengurangi dampak banjir adalah melakukan pemantauan terhadap curah hujan dan ketinggian air. Informasi tersebut dapat digunakan untuk memperkirakan tingkat risiko banjir sehingga masyarakat dapat lebih waspada terhadap kemungkinan terjadinya banjir.

Berdasarkan materi *“Bridging Global Infrastructure to Address Local Challenges in High Performance Computing (HPC)”* yang disampaikan oleh Dr. Warawan Dias Carbalo dari Thammasat University, teknologi komputasi dapat dimanfaatkan untuk membantu menyelesaikan permasalahan lokal melalui pengolahan data dan pemodelan komputasi. Materi tersebut juga menekankan pentingnya kualitas data, integrasi teknologi, dan kerja sama berbagai bidang dalam menghasilkan solusi yang bermanfaat.

Oleh karena itu, studi kasus ini mengangkat simulasi prediksi risiko banjir di wilayah Bengkulu menggunakan bahasa pemrograman Python. Program memanfaatkan data curah hujan dan ketinggian air untuk mengklasifikasikan tingkat risiko banjir menjadi rendah, sedang, atau tinggi.

## 2. Rumusan Masalah

Bagaimana memanfaatkan data curah hujan dan ketinggian air untuk mengidentifikasi tingkat risiko banjir secara sederhana menggunakan program Python?

## 3. Tujuan

1. Mengolah data curah hujan dan ketinggian air sebagai indikator risiko banjir.
2. Mengklasifikasikan risiko banjir menjadi tiga kategori, yaitu rendah, sedang, dan tinggi.
3. Menghasilkan informasi dan saran sederhana berdasarkan kategori risiko.
4. Menerapkan konsep pemanfaatan komputasi untuk membantu menyelesaikan permasalahan lingkungan lokal.

## 4. Solusi yang Diusulkan

Solusi yang diusulkan adalah membuat program Python yang menerima masukan berupa nama wilayah, curah hujan dalam milimeter (mm), dan ketinggian air dalam sentimeter (cm). Program kemudian memeriksa nilai masukan dan menentukan kategori risiko berdasarkan aturan yang telah ditetapkan.

Hasil klasifikasi ditampilkan melalui terminal, disertai saran tindakan sederhana sesuai dengan tingkat risiko yang diperoleh.

## 5. Alur Kerja Sistem

1. **Input data:** Pengguna memasukkan nama wilayah, curah hujan, dan ketinggian air.
2. **Validasi data:** Program memeriksa agar nilai curah hujan dan ketinggian air tidak negatif.
3. **Pengolahan data:** Program membandingkan nilai masukan dengan batas kategori risiko.
4. **Klasifikasi risiko:** Sistem menentukan kategori rendah, sedang, atau tinggi.
5. **Output:** Program menampilkan hasil klasifikasi beserta saran yang sesuai.

## 6. Aturan Klasifikasi Risiko

| Kondisi | Kategori Risiko |
|---|---|
| Curah hujan ≥ 100 mm atau ketinggian air ≥ 150 cm | Tinggi |
| Curah hujan ≥ 50 mm atau ketinggian air ≥ 80 cm, tetapi tidak termasuk kategori tinggi | Sedang |
| Curah hujan < 50 mm dan ketinggian air < 80 cm | Rendah |

**Catatan:** Batas tersebut merupakan aturan simulasi untuk keperluan pembelajaran, bukan ambang batas resmi dari lembaga kebencanaan.

## 7. Teknologi yang Digunakan

- **Bahasa pemrograman:** Python
- **Editor:** Visual Studio Code
- **Media keluaran:** Terminal
- **Pengelolaan proyek:** Git dan GitHub
- **Data simulasi:** CSV

Program menggunakan fitur dasar Python sehingga dapat dijalankan tanpa memasang pustaka tambahan.

## 8. Hasil yang Diharapkan

Program diharapkan dapat membantu pengguna memahami cara mengolah data lingkungan menjadi informasi risiko yang mudah dibaca. Sebagai contoh, ketika curah hujan mencapai 65 mm dan ketinggian air mencapai 90 cm, program mengategorikan risiko sebagai sedang karena ketinggian air telah mencapai batas kategori sedang, tetapi belum mencapai batas kategori tinggi.

Hasil tersebut disertai saran untuk memantau perubahan kondisi lingkungan. Dengan demikian, program memperlihatkan bagaimana data dapat diolah menjadi informasi pendukung pengambilan keputusan.

## 9. Hubungan dengan Materi HPC

Studi kasus ini mengadaptasi gagasan utama materi pemateri, yaitu pemanfaatan teknologi komputasi untuk menyelesaikan permasalahan lokal. Pengolahan data lingkungan menjadi informasi risiko merupakan contoh sederhana penerapan gagasan tersebut.

Namun, implementasi ini masih berupa simulasi berbasis aturan dan belum menggunakan High Performance Computing (HPC), komputasi paralel, sensor IoT, maupun model kecerdasan buatan. Teknologi tersebut dapat dipertimbangkan sebagai pengembangan lanjutan apabila tersedia data yang memadai dan kebutuhan komputasi yang sesuai.

## 10. Keterbatasan dan Pengembangan

Program ini memiliki beberapa keterbatasan. Data yang digunakan merupakan data simulasi, sedangkan batas klasifikasi ditentukan secara sederhana. Program juga belum mempertimbangkan faktor lain seperti kondisi drainase, topografi, durasi hujan, dan karakteristik daerah aliran sungai.

Pengembangan selanjutnya dapat mencakup penggunaan data historis banjir yang valid, integrasi sensor ketinggian air dan curah hujan, visualisasi peta berbasis GIS, serta pengujian model prediksi menggunakan data nyata. Untuk mendukung penggunaan dalam sistem peringatan dini, model harus divalidasi dan dikembangkan bersama pihak yang memiliki keahlian di bidang hidrologi dan kebencanaan.

## 11. Kesimpulan

Simulasi prediksi risiko banjir di wilayah Bengkulu merupakan contoh penerapan pemrograman Python untuk mengolah data lingkungan menjadi informasi yang mudah dipahami. Proyek ini menunjukkan tahapan dasar pengolahan data, klasifikasi risiko, dan penyajian hasil sebagai pendukung pengambilan keputusan. Walaupun belum menerapkan HPC secara langsung, studi kasus ini dapat menjadi langkah awal untuk memahami bagaimana teknologi komputasi dapat dikembangkan guna membantu menangani permasalahan lingkungan di tingkat lokal.
