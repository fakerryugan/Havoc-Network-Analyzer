from flask import Flask, render_template, request
import pandas as pd
import math
from collections import Counter
import os
import time

app = Flask(__name__)

print("--- MEMULAI SERVER ---")
print("1. Sedang memuat dataset...")

def extract_ports(info_str):
    try:
        
        if ">" in info_str:
            parts = info_str.split(">")
            src = parts[0].strip()
            
            dst = parts[1].strip().split(' ')[0]
            if src.isdigit() and dst.isdigit():
                return int(src), int(dst)
        return 0, 0
    except:
        return 0, 0


files = {
    "Social Media": "socmed.csv",
    "Browsing": "browse.csv",
    "YouTube": "youtube.csv"
}

data_list = []
total_rows = 0


for label, filename in files.items():
    if os.path.exists(filename):
        try:
            df = pd.read_csv(filename)
            
            df['Info'] = df['Info'].astype(str) 
            
            ports = df['Info'].apply(extract_ports)
            df['SrcPort'] = [x[0] for x in ports]
            df['DstPort'] = [x[1] for x in ports]
            df['Label'] = label  
            
            df = df[(df['SrcPort'] != 0) & (df['DstPort'] != 0)]
            
            
            df = df[['Length', 'SrcPort', 'DstPort', 'Label']]
            
            data_list.append(df)
            print(f"   [OK] {filename}: {len(df)} data valid dimuat.")
        except Exception as e:
            print(f"   [ERROR] Gagal membaca {filename}: {e}")
    else:
        print(f"   [MISSING] File {filename} tidak ditemukan.")


if data_list:
    data = pd.concat(data_list, ignore_index=True)
    total_rows = len(data)
    print(f"2. Total Data Training: {total_rows} baris.")
else:
    data = pd.DataFrame(columns=['Length', 'SrcPort', 'DstPort', 'Label'])
    print("2. [PERINGATAN] Tidak ada data yang dimuat.")


print("3. Melakukan Normalisasi Data...")
feature_cols = ['Length', 'SrcPort', 'DstPort']
data_scaled = data.copy()
min_max_vals = {}

for col in feature_cols:
    if not data.empty:
        min_val = data[col].min()
        max_val = data[col].max()
    else:
        min_val, max_val = 0, 1
        
    min_max_vals[col] = (min_val, max_val)
    
    
    if max_val != min_val:
        data_scaled[col] = (data[col] - min_val) / (max_val - min_val)
    else:
        data_scaled[col] = 0.0


X_train = data_scaled[feature_cols].values.tolist()
y_train = data_scaled['Label'].tolist()

print("--- SERVER SIAP DIGUNAKAN ---\n")
def euclidean_distance(row1, row2):

    distance = 0.0
    for i in range(len(row1)):
        distance += (row1[i] - row2[i])**2
    return math.sqrt(distance)

def knn_predict(input_user, k=5):
    if not X_train: return "Error: Database Kosong"
    
    distances = []

    for i in range(len(X_train)):
        dist = euclidean_distance(X_train[i], input_user)
        distances.append((dist, y_train[i]))
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]
    neighbor_labels = [label for dist, label in neighbors]
    vote_result = Counter(neighbor_labels)
    
    
    
    prediction = vote_result.most_common(1)[0][0]
    
    return prediction




@app.route('/', methods=['GET', 'POST'])
def index():
    prediksi = None
    input_data = None
    waktu_proses = 0
    
    if request.method == 'POST':
        try:
            start_time = time.time()
            
            
            l = float(request.form['length'])
            s = float(request.form['src_port'])
            d = float(request.form['dst_port'])
            
            input_data = {'Length': l, 'Src': s, 'Dst': d}
            
            
            input_norm = []
            raw_input = [l, s, d]
            
            for i, col in enumerate(feature_cols):
                min_v, max_v = min_max_vals[col]
                if max_v != min_v:
                    norm_val = (raw_input[i] - min_v) / (max_v - min_v)
                else:
                    norm_val = 0.0
                input_norm.append(norm_val)
            
            
            prediksi = knn_predict(input_norm, k=5)
            
            waktu_proses = round(time.time() - start_time, 4)
            
        except ValueError:
            prediksi = "Error: Input harus angka."

    return render_template('index.html', prediction=prediksi, input=input_data, time=waktu_proses)

if __name__ == '__main__':
    app.run(debug=True)