# 1
# data = [23, 57, 76, 6, 60, 28, 30,
#         44, 85, 44, 97, 32, 71, 85,
#         46, 95, 29, 37, 13, 79, 15, 9,
#         23, 10, 22, 78, 46, 2, 99, 3]

# # Inisialisasi nilai maksimum dan minimum dengan elemen pertama
# max_num = data[0]
# min_num = data[0]

# # Loop untuk mencari nilai maksimum dan minimum
# for num in data:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# # Output hasil
# print("Max number:", max_num)
# print("Min number:", min_num)

# 2
# id_list = [
#     'K0QY6', 'fJU08', 'K0QY6', 'VeZrS', 'jxjQ6', 'sjqom', 'AefAN', 'jxjQ6',
#     'S90wn', 'FZw7F', 'lgYbm', 'dD1ZM', 'sjqom', 'dD1ZM', 'fJU08', 'AefAN',
#     'jxjQ6', 'K0QY6', 'prdDz', 'dD1ZM', 'AefAN', 'WfgpU', 'VeZrS', 'sjqom'
# ]

# # Buat list kosong untuk menyimpan ID unik
# id_unik = []

# for id in id_list:
#     # Jika ID belum ada dalam id_unik, tambahkan ke sana
#     if id not in id_unik:
#         id_unik.append(id)

# # Hitung dan tampilkan jumlah ID unik
# print("Jumlah ID unik adalah:", len(id_unik))

# 3
# list = [
#     344, 838, 502, 262, 590, 959, 151, 491, 71, 980, 156, 13, 280, 615, 278, 185,
#     851, 599, 947, 598, 961, 534, 633, 751, 836, 446, 7, 956, 335, 765, 600, 428,
#     595, 478, 667, 628, 375, 402, 663, 728, 704, 182, 377, 380, 49, 253, 566,
#     662, 492, 930, 285, 5, 467, 496, 421, 317, 774, 86, 942, 149, 270, 765, 357,
#     373, 336, 63, 976, 509, 863, 139, 504, 321, 635, 96, 977, 538, 552, 683, 83,
#     752, 576, 350, 538, 79, 164, 414, 579, 948, 971, 121, 354, 562, 562, 63, 385,
#     185, 731, 872, 342, 898
# ]

# # List untuk menyimpan square number
# square_numbers = []

# # Mengecek setiap angka apakah merupakan square number
# for number in list:
#     akar = int(number ** 0.5)  # Hitung akar kuadrat dari angka
#     if akar * akar == number:
#         square_numbers.append(number)

# # Tampilkan hasil
# print("Total square number:", len(square_numbers))
# print(square_numbers)

# 4
# Fungsi untuk menghitung tingkat kesamaan dua daftar film
# def hitung_kesamaan(daftar1, daftar2):
#     # Ubah string menjadi list, bersihkan spasi, dan ubah ke huruf kecil
#     list1 = daftar1.lower().split(',')
#     list2 = daftar2.lower().split(',')
    
#     # Hapus spasi tambahan dari setiap judul
#     list1 = [film.strip() for film in list1]
#     list2 = [film.strip() for film in list2]

#     # Buat set (kumpulan unik) dari masing-masing list
#     set1 = set(list1)
#     set2 = set(list2)

#     # Hitung jumlah film yang sama
#     sama = set1.intersection(set2)
#     jumlah_sama = len(sama)

#     # Hitung jumlah total film unik (gabungan)
#     total_film = len(set1.union(set2))

#     # Hitung persentase kesamaan
#     if total_film > 0:
#         persentase = (jumlah_sama / total_film) * 100
#     else:
#         persentase = 0

#     # Tampilkan hasil dengan dua angka di belakang koma
#     print(f"Similarity level {persentase:.2f}%")

# # Contoh penggunaan
# print("Example 1")
# fav1 = "'Witch Of Stone', 'Mice And Soldiers', 'Learning From The Ashes', 'Assassins Of Sorrow', 'Wand Of Next Year', 'Binding To Dreams'"
# teman1 = "'Soldiers And Visitors', 'Intelligence In Orbit', 'Wand Of Next Year', 'Birth Of The Sands', 'Assassins Of Sorrow'"
# hitung_kesamaan(fav1, teman1)

# print("\nExample 2")
# fav2 = "'Horrors And Figures','Foreigner In The Library', ' Learning From The Ashes','Assassins Of Sorrow', 'Wand Of Next Year', 'Oblivious To The Country'"
# teman2 = "'Soldiers And Visitors','Intelligence In Orbit', 'wand of next year','horrors and figures', 'assassins of sorrow'"
# hitung_kesamaan(fav2, teman2)
