# 📓 Catatan Kuliah: Minggu 03 - AI Klasifikasi (ML)

**Nama: Hafizh Hilman Asyhari**
**Major: Informatics Engineering**
**Tanggal: 27 September 2025** [Tanggal Kuliah]

## Poin Utama Kuliah

* **Apa itu AI (Machine Learning)?** Daripada kita menulis aturan `IF-THEN` secara manual, kita "mengajari" mesin untuk *belajar* aturannya sendiri dari data.
* **Supervised vs. Unsupervised Learning:**
    * **Supervised (Terawasi):** Data kita punya "label" / "jawaban". Kita melatih model untuk memprediksi label itu.
        * **Klasifikasi:** Labelnya kategori (misal: "Karang Sehat", "Karang Sakit").
        * **Regresi:** Labelnya angka (misal: memprediksi *berapa* suhu laut besok).
    * **Unsupervised (Tak Terawasi):** Data tidak punya label. Kita minta mesin mencari pola (misal: *Clustering* nelayan berdasarkan lokasi tangkapan).
* **Fokus Hari Ini: Klasifikasi.** Contoh: Memakai data (Suhu, Salinitas, Arus) untuk memprediksi apakah besok akan terjadi `blooming_alga` (Ya/Tidak).

## Istilah Kunci & Definisi

* **Scikit-learn (sklearn):** "Kitab suci" ML di Python. Semua *tools* ada di sini.
* **Model:** Algoritma yang kita pilih (misal: `LogisticRegression`, `KNeighborsClassifier`).
* **`train_test_split()`:** Fungsi paling penting. Kita harus membagi data kita: 80% untuk "melatih" model (data latih), 20% untuk "menguji" model (data uji).
* **Akurasi (Accuracy):** Metrik paling sederhana. Berapa % tebakan model yang benar? (Jangan hanya andalkan ini, kata dosen).

## Catatan Tambahan

* Alur kerja ML standar:
    1.  Muat Data (Pandas)
    2.  Bersihkan Data (isi `NaN`, buang *outlier*)
    3.  Tentukan Fitur (X) dan Target (y)
    4.  Bagi Data (`train_test_split`)
    5.  Pilih Model (misal: `LogisticRegression`)
    6.  Latih Model (`model.fit(X_train, y_train)`)
    7.  Evaluasi Model (`model.score(X_test, y_test)`)
* Dosen bilang: "Garbage in, garbage out." Kualitas data (langkah 1-2) 80% lebih penting daripada pemilihan model (langkah 5).
