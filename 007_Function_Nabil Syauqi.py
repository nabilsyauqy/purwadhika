# 1
# # Fungsi untuk menghitung rata-rata
# def avg(list_angka):
#     jumlah = sum(list_angka)       # Menjumlahkan semua angka di dalam list
#     banyak_data = len(list_angka)  # Menghitung jumlah data dalam list
#     rata_rata = jumlah / banyak_data
#     return rata_rata

# list_angka = [5, 6, 3, -1, -3, 5]
# print(avg(list_angka))  # Output: 2.5

# 2
# def gcd(a, b):
#     # Cek apakah input valid
#     if a <= 0 or b <= 0:
#         print("Input cannot be zero or negative")
#         return

#     # Simpan nilai asli untuk keperluan print
#     x, y = a, b

#     # Proses Euclidean untuk mencari GCD
#     while b != 0:
#         a, b = b, a % b

#     if a == 1:
#         print(f"{x} and {y} are coprime number")
#         return
#     else:
#         return a

# # Contoh penggunaan
# print(gcd(15, 25))  # Output: 5
# print(gcd(9, 7))    # Output: "9 and 7 are coprime number" lalu None
# print(gcd(0, 1))    # Output: "Input cannot be zero or negative" lalu None

# 3
# def isLeapYear(year):
#     # Jika tahun habis dibagi 400, maka tahun kabisat
#     if year % 400 == 0:
#         return True
#     # Jika tahun habis dibagi 100, maka bukan tahun kabisat
#     elif year % 100 == 0:
#         return False
#     # Jika tahun habis dibagi 4, maka tahun kabisat
#     elif year % 4 == 0:
#         return True
#     # Selain itu, bukan tahun kabisat
#     else:
#         return False

# # Pengujian (assertion)
# assert isLeapYear(1999) == False
# assert isLeapYear(2000) == True
# assert isLeapYear(2001) == False
# assert isLeapYear(2004) == True
# assert isLeapYear(2100) == False
# assert isLeapYear(2400) == True

# print("Semua test berhasil!")

# 4
