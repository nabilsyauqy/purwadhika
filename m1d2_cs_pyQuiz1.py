# Program Menghitung IMT (Indeks Massa Tubuh)

try:
    
    tinggi_cm = float(input("Masukkan tinggi badan (dalam sentimeter, contoh: 170): "))
    berat_kg = float(input("Masukkan berat badan (dalam kilogram): "))

    if tinggi_cm <= 0 or berat_kg <= 0:
        print("Tinggi dan berat badan harus lebih dari 0.")
    else:
        
        tinggi_m = tinggi_cm / 100

        # Menghitung IMT
        imt = berat_kg / (tinggi_m ** 2)

        # Klasifikasi IMT
        if imt < 18.5:
            kategori = "Kekurangan Berat Badan"
        elif 18.5 <= imt <= 24.9:
            kategori = "Normal"
        elif 25 <= imt <= 29.9:
            kategori = "Berat Badan Berlebih"
        else:
            kategori = "Obesitas"

        # Tampilkan hasil
        print("\nHasil Perhitungan IMT:")
        print(f"IMT Anda adalah: {imt:.2f}")
        print(f"Kategori: {kategori}")

except ValueError:
    print("Input tidak valid. Masukkan angka dengan benar.")
