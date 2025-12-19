# 🛡️ Havoc Network Analyzer (V.4.0)

**Havoc Network Analyzer** adalah aplikasi analisis lalu lintas jaringan berbasis web yang menggunakan algoritma **K-Nearest Neighbors (KNN)** untuk mengklasifikasikan tipe penggunaan data (Social Media, Browsing, atau YouTube).

Sistem ini dibangun menggunakan **Flask** dan mengimplementasikan logika KNN secara manual (from scratch) tanpa bergantung pada library machine learning eksternal seperti Scikit-Learn untuk proses prediksinya.

---

## 🚀 Fitur Utama

-   **Manual KNN Implementation**: Menggunakan perhitungan *Euclidean Distance* murni untuk klasifikasi data.
-   **Auto Data Normalization**: Melakukan *Min-Max Scaling* otomatis pada fitur `Length`, `SrcPort`, dan `DstPort`.
-   **Cyberpunk Interface**: UI futuristik yang responsif dengan tema visual "Havoc System".
-   **Real-time Processing**: Menampilkan hasil prediksi beserta durasi waktu pemrosesan data.

---

## 🛠️ Tech Stack

-   **Backend**: Python, Flask
-   **Data Processing**: Pandas
-   **Frontend**: HTML5, CSS3 (Google Fonts: Teko, Rajdhani)
-   **Math**: Euclidean Distance & Min-Max Normalization

---

## 📂 Struktur Repositori

```text
.
├── app.py              # Logika Utama & Algoritma KNN
├── templates/
│   └── index.html      # Tampilan UI (Cyberpunk Theme)
├── static/
│   └── logo.png        # Logo aplikasi
├── socmed.csv          # Dataset untuk kategori Social Media
├── browse.csv          # Dataset untuk kategori Browsing
├── youtube.csv         # Dataset untuk kategori YouTube
└── README.md           # Dokumentasi proyek
⚙️ Cara MenjalankanPersiapan DatasetPastikan file socmed.csv, browse.csv, dan youtube.csv berada di folder utama. Dataset harus memiliki kolom Length dan Info (dengan format port Source > Destination).Install DependensiPastikan Python sudah terinstal, lalu jalankan perintah:Bashpip install flask pandas
Jalankan ServerBashpython app.py
Akses AplikasiBuka browser dan buka alamat: http://127.0.0.1:5000📊 Logika PerhitunganSistem menggunakan rumus Euclidean Distance untuk mencari tetangga terdekat:$$d = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}$$Serta Min-Max Normalization untuk menyamakan skala data:$$x' = \frac{x - \text{min}(x)}{\text{max}(x) - \text{min}(x)}$$📸 Tampilan Interface(Silakan upload screenshot aplikasi kamu di sini)Developed with ❤️ by [Nama Kamu]
---

### Tips untuk GitHub:
1. **Gambar Preview**: Pada bagian `📸 Tampilan Interface`, ganti link placeholder tersebut dengan link gambar asli hasil screenshot aplikasimu agar terlihat lebih keren.
2. **Koleksi Data**: Pastikan file CSV kamu tidak terlalu besar agar saat di-push ke GitHub tidak terkena limit ukuran file.

**Apakah ada bagian spesifik seperti cara kerja ekstraksi port yang ingin kamu jela
