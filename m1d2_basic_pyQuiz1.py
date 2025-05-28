# Lengkapilah program berikut ini untuk menghitung total gaji harian seorang pegawai berdasarkan:
# - Nama pegawai
# - Jumlah jam kerja
# - Tarif per jam
# 
# Program juga harus membuat ID pegawai otomatis berdasarkan inisial nama dan total jam kerja.


print("=== Program Kalkulator Gaji Harian ===")

# TODO: Ambil input nama pegawai
nama = input("Masukkan nama pegawai: ")

# TODO: Ambil input jumlah jam kerja (int)
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

# TODO: Ambil input tarif per jam (float)
tarif_per_jam = float(input("Masukkan tarif per jam: "))

# TODO: Hitung total gaji
total_gaji = jam_kerja * tarif_per_jam

# TODO: Buat ID pegawai dari 3 huruf pertama nama + jam kerja
inisial = nama[:3].upper()
id_pegawai = f"{inisial}{jam_kerja}"

# TODO: Tampilkan hasil
print("\n=== Hasil Perhitungan Gaji ===")
print("ID Pegawai        :", id_pegawai)
print("Nama              :", nama)
print("Jumlah Jam Kerja  :", jam_kerja)
print("Tarif Per Jam     :",tarif_per_jam)
print("Total Gaji : Rp", format(total_gaji, ",.2f"))
