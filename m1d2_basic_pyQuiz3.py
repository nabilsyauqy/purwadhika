import math

# Input dari pengguna
total_hari = int(input("Masukkan jumlah hari: "))

# Konstanta konversi
hari_per_tahun = 360
hari_per_bulan = 30
hari_per_minggu = 7

# Hitung jumlah tahun
tahun = math.floor(total_hari / hari_per_tahun)
sisa_hari = total_hari - (tahun * hari_per_tahun)

# Hitung jumlah bulan
bulan = math.floor(sisa_hari / hari_per_bulan)
sisa_hari = sisa_hari - (bulan * hari_per_bulan)

# Hitung jumlah minggu
minggu = math.floor(sisa_hari / hari_per_minggu)
hari = math.ceil(total_hari % hari_per_tahun % hari_per_bulan / hari_per_minggu)
#hari = sisa_hari - (minggu * hari_per_minggu)
# Tampilkan hasil akhir
print(f"{tahun} Tahun {bulan} Bulan {minggu} Minggu {hari} Hari")

