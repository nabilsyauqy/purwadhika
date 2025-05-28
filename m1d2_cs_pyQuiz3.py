print("=== Sistem Penyaringan Responden Survei ===")


nama = input("Masukkan nama lengkap: ")
usia = int(input("Masukkan usia Anda: "))
kota = input("Kota domisili: ").lower()
internet_harian = int(input("Berapa jam per hari Anda menggunakan internet?: "))
bersedia = input("Apakah Anda bersedia mengisi survei? (ya/tidak): ").lower()


layak = False
reward = 0

# TODO: Tambahkan pengecekan kelayakan
# Syarat:
# - Usia antara 18–45 tahun
# - Domisili di kota target: jakarta, bandung, surabaya
# - Penggunaan internet minimal 2 jam/hari
# - Menjawab "ya" untuk kesediaan

kota_target = ["jakarta", "bandung", "surabaya"]
if (18 <= usia <= 45) and (kota in kota_target) and (internet_harian >= 2) and (bersedia == "ya"):
    layak = True
    print(f"\n{nama} lolos sebagai responden.")

    # TODO: Estimasi reward
    # Jika internet_harian >= 5 -> reward = 50000
    # Jika 3 ≤ internet_harian < 5 -> reward = 35000
    # Jika < 3 -> reward = 20000

    if internet_harian >= 5:
        reward = 50000
    elif 3 <= internet_harian < 5:
        reward = 35000
    else:
        reward = 20000

    # TODO: Cetak ringkasan hasil
    print(f"Estimasi reward untuk {nama} adalah Rp{reward:,}")
else:
    print(f"\nMaaf {nama}, Anda tidak memenuhi kriteria responden.")

print("\n=== Proses Seleksi Selesai ===")
