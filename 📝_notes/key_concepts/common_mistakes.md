# 🤦 Kesalahan Umum (Common Mistakes)

* **`FileNotFoundError`:** Kesalahan paling sering. Path (jalur) file salah.
    * Solusi: Pastikan tahu *working directory* (direktori kerja) notebook. Cek `os.getcwd()`. Gunakan path relatif.
* **Data Leakage (Kebocoran Data) di ML:**
    * Kesalahan: Melakukan *scaling* atau mengisi `NaN` **sebelum** `train_test_split`.
    * Akibat: Model "belajar" dari data uji secara tidak langsung. Akurasi terlihat bagus (99%), tapi saat dipakai di data baru, hancur.
    * Solusi: **Selalu** `train_test_split` dulu! `fit_transform` di data latih, tapi **hanya** `transform` di data uji.
* **Beda CRS di Geopandas:**
    * Kesalahan: Mencoba menggabungkan data poligon (misal: area konservasi) dengan data titik (misal: lokasi kapal) yang punya CRS berbeda.
    * Akibat: Peta hancur, titiknya melayang di antah berantah.
    * Solusi: Cek `gdf.crs`. Samakan keduanya pakai `gdf = gdf.to_crs("EPSG:4326")`.
* **Menyimpan API Key di Kode (!!!):**
    * Kesalahan: Menulis `API_KEY = "abc12345..."` langsung di file `.ipynb` lalu di-push ke GitHub.
    * Akibat: Kunci API dicuri *bot* dalam hitungan detik.
    * Solusi: Gunakan file `.env` dan *library* `python-dotenv`. Masukkan `.env` ke `.gitignore`.
* **Overfitting (Model Terlalu Pintar):**
    * Gejala: Akurasi data latih 99%, akurasi data uji 70%.
    * Artinya: Model "menghafal" data latih, bukan "belajar" polanya.
    * Solusi: Gunakan model yang lebih sederhana, tambah data, atau gunakan teknik regularisasi.
