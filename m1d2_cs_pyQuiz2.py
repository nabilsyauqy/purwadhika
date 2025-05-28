print("=== Selamat datang di Sistem Pembelian Tiket ===")


nama = input("Masukkan nama lengkap: ")
umur_input = input("Masukkan umur: ")
email = input("Masukkan email: ")
jml_tiket_input = input("Masukkan jumlah tiket: ")

print("\n=== Validasi Data ===")
boleh_daftar = True  # Default boleh daftar

# Validasi umur
try:
    umur = int(umur_input)
    if umur >= 17:
        print("Umur valid.")
    else:
        print("Umur kamu belum cukup untuk mendaftar.")
        boleh_daftar = False
except ValueError:
    print("Umur harus berupa angka.")
    boleh_daftar = False

# Validasi email
if "@" in email and "." in email:
    print("Email valid.")
else:
    print("Format email tidak sesuai.")
    boleh_daftar = False

# Validasi nama
if len(nama.strip()) > 0:
    print("Nama tercatat.")
else:
    print("Nama tidak boleh kosong.")
    boleh_daftar = False

# Validasi jumlah tiket
try:
    jml_tiket = int(jml_tiket_input)
    if jml_tiket <= 0:
        print("Jumlah tiket harus lebih dari 0.")
        boleh_daftar = False
except ValueError:
    print("Jumlah tiket harus berupa angka.")
    boleh_daftar = False

# Proses akhir jika data valid
if boleh_daftar:
    print("\n=== Total Harga Tiket ===")
    harga_tiket = 100_000
    total_harga = jml_tiket * harga_tiket

    if jml_tiket > 2:
        diskon = total_harga * 0.2
        print("Selamat kamu mendapatkan diskon 20%!")
        total_harga -= diskon

    print(f"Rp. {harga_tiket} x {jml_tiket} = Rp. {total_harga:,.0f}")
    print("\nPendaftaran berhasil! Sampai jumpa di acara.")
else:
    print("\nPendaftaran gagal. Silakan periksa data kamu.")
