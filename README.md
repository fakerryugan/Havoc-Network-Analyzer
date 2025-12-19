# 👺 HAVOC NETWORK ANALYZER (V.1.0)
> **CYBER-TRAFFIC CLASSIFICATION SYSTEM USING K-NEAREST NEIGHBORS**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-black.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

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

