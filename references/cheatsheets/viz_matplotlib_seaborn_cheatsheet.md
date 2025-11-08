# Ringkasan: Matplotlib & Seaborn

**oleh : Hafizh Hilman Asyhari (hafizhhasyhari)**
Github : hafizhhasyhari
**Tahun : 2025**

import matplotlib.pyplot as plt
import seaborn as sns

# --- Matplotlib (plt) ---
# Fungsional (Cepat & Mudah)
plt.plot(x, y)
plt.title('Judul')
plt.xlabel('Label X')
plt.ylabel('Label Y')
plt.show()

# Object-Oriented (Disarankan, Lebih Fleksibel)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, label='Data 1', color='blue', linestyle='--', marker='o')
ax.set_title('Judul')
ax.set_xlabel('Label X')
ax.set_ylabel('Label Y')
ax.legend()
plt.show()

# Tipe Plot Umum (plt)
plt.scatter(x, y) # Scatter Plot
plt.bar(x, y)     # Bar Plot
plt.hist(data, bins=30) # Histogram
plt.pie(data, labels=labels) # Pie Chart

# --- Seaborn (sns) ---
# Dibangun di atas Matplotlib, lebih mudah utk statistik

# Scatter Plot (dgn Kategori)
sns.scatterplot(data=df, x='kolom_x', y='kolom_y', hue='kategori')

# Line Plot
sns.lineplot(data=df, x='tanggal', y='suhu')

# Bar Plot (Otomatis menghitung rata-rata)
sns.barplot(data=df, x='kategori', y='nilai')

# Box Plot (Distribusi)
sns.boxplot(data=df, x='kategori', y='nilai')

# Violin Plot (Boxplot + Distribusi)
sns.violinplot(data=df, x='kategori', y='nilai')

# Histogram
sns.histplot(data=df, x='kolom', kde=True) # kde=True (tambah garis densitas)

# Heatmap (Peta Panas / Matriks Korelasi)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')

# Pair Plot (Melihat hubungan semua kolom)
sns.pairplot(df, hue='kategori')
