import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Muat Data
df = pd.read_csv('data/data_latih.csv') # Asumsi data sudah bersih

# 2. Tentukan Fitur (X) dan Target (y)
# Asumsi 'kesehatan_karang' adalah target (0 = Sakit, 1 = Sehat)
X = df.drop('kesehatan_karang', axis=1)
y = df['kesehatan_karang']
# Pastikan X hanya berisi angka (jika belum, lakukan encoding)

# 3. Bagi Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Shape Latih: {X_train.shape} | Shape Tes: {X_test.shape}")

# 4. Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Latih Model
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)

# 6. Evaluasi
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAkurasi Model: {accuracy * 100:.2f}%")
print("\nLaporan Klasifikasi:")
print(classification_report(y_test, y_pred))

# 7. (Opsional) Simpan Model
import joblib
joblib.dump(model, 'model/model_karang_rf.pkl')
joblib.dump(scaler, 'model/scaler_karang.pkl')
print("\nModel dan scaler berhasil disimpan.")
