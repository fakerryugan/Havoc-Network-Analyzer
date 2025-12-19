# 👺 HAVOC NETWORK ANALYZER (V.4.0)
> **CYBER-TRAFFIC CLASSIFICATION SYSTEM USING K-NEAREST NEIGHBORS**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-black.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## ⚡ Overview
**Havoc Network Analyzer** adalah sistem klasifikasi trafik jaringan berbasis web yang mampu mengenali jenis aktivitas data (Social Media, Browsing, YouTube) secara *real-time*. Proyek ini mendemonstrasikan bagaimana algoritma **Machine Learning** dapat diimplementasikan secara murni (*from scratch*) tanpa bantuan library seperti Scikit-Learn.

---

## 🎨 System Interface Design
Antarmuka didesain dengan estetika **Cyberpunk/High-Tech Interface** (Danjin Red Theme) untuk memberikan pengalaman visual "Hacker/Analyst".

| Main Dashboard | Logic Process |
| :---: | :---: |
| ![Preview](https://via.placeholder.com/250x450.png?text=Cyberpunk+UI+Design) | ![Process](https://via.placeholder.com/250x450.png?text=Result+Overlay+Animation) |

---

## 🧠 Brain of Havoc: Teknikal & Algoritma

Sistem ini bekerja dengan memproses paket data melalui 3 tahap utama:

### 1. Feature Extraction (Regex-like Parsing)
Aplikasi membedah kolom `Info` pada dataset Wireshark untuk mengambil port sumber dan tujuan secara otomatis:
```python
# Contoh alur ekstraksi:
# "443 > 51234 [ACK]" -> SrcPort: 443, DstPort: 51234
2. Min-Max Normalization
Agar port (0-65535) dan panjang paket tidak timpang, data diskalakan ke rentang 0 hingga 1:

x 
scaled
​
 = 
x 
max
​
 −x 
min
​
 
x−x 
min
​
 
​
 
3. K-Nearest Neighbors (KNN) logic
Sistem menghitung jarak "kemiripan" antara input user dengan ribuan data di database menggunakan Euclidean Distance:

d(p,q)= 
(p 
1
​
 −q 
1
​
 ) 
2
 +(p 
2
​
 −q 
2
​
 ) 
2
 +(p 
n
​
 −q 
n
​
 ) 
2
 

​
 
🛠️ Tech Architecture
Komponen	Teknologi	Deskripsi
Engine	Python 3	Inti pemrosesan logika KNN.
Web Server	Flask	Menangani routing dan request HTTP.
Data Handler	Pandas	Manajemen dataset CSV skala besar.
UI/UX	CSS Grid & Flex	Desain futuristik dengan font Rajdhani & Teko.

Ekspor ke Spreadsheet

📂 Folder Structure
Bash

📁 havoc-network-analyzer
├── 📄 app.py              # The Machine Learning Engine
├── 📁 templates           # UI Components
│   └── 📄 index.html      # Cyberpunk Dashboard
├── 📁 static              # Assets
│   └── 🖼️ logo.png        # Branding
├── 📊 browse.csv          # Training Data: Browsing
├── 📊 socmed.csv          # Training Data: Social Media
└── 📊 youtube.csv         # Training Data: Video Streaming
🚀 Installation & Quick Start
Clone the project

Bash

git clone [https://github.com/username/havoc-analyzer.git](https://github.com/username/havoc-analyzer.git)
Setup environment

Bash

pip install flask pandas
Fire up the engine

Bash

python app.py
Access the console Buka http://localhost:5000 di browser favoritmu.

📌 Development Roadmap
[x] KNN Manual Implementation

[x] Normalization Engine

[x] Cyberpunk UI Design

[ ] Integration with Live Wireshark Capture (Next Update)

[ ] Support for Multi-label classification

Developed by [Nama Kamu] Building the future of network analysis, one packet at a time.


### Apa yang saya tambahkan:
1.  **Badges**: Menambahkan label visual di atas agar terlihat seperti repositori profesional.
2.  **Tabel Arsitektur**: Memudahkan orang memahami teknologi apa saja yang kamu gunakan.
3.  **Matematika LaTeX**: Menjelaskan rumus Normalisasi dan Euclidean agar kamu terlihat ahli dalam data science.
4.  **Roadmap**: Memberi kesan bahwa proyek ini akan terus berkembang.
5.  **Visual Structure**: Menggunakan ikon folder agar struktur file mudah dibaca.

**Apakah ada bagian dari algoritmanya (seperti nilai K=5) yang ingin kamu tonjolkan lebih berani lagi desainnya?**
