print("=== Kalkulator Profil Produk ===")

# Input User
produk = input("Masukkan nama produk: ")
harga = float(input("Masukkan harga satuan produk: "))
jumlah = int(input("Masukkan jumlah produk yang dibeli: "))
diskon = float(input("Masukkan diskon (dalam persen): "))

# nama produk
nama_format = produk.upper()

# total sebelum diskon
total = harga * jumlah

# besar diskon
nilai_diskon = total * (diskon / 100)

# total akhir
total_akhir = total - nilai_diskon

# hasil
print("\n=== Ringkasan Pembelian ===")
print("Produk:", nama_format)
print("Total sebelum diskon: Rp{:,.2f}".format(total))
print("Diskon: Rp{:,.2f}".format(nilai_diskon))
print("Total yang harus dibayar: Rp{:,.2f}".format(total_akhir))
