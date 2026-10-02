# Nama File: deret_3_6_9.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Menentukan bilangan ke-n dari deret 3, 6, 9, 12, 15, 18, ...

# Definisi dan Spesifikasi
# SukuKelipatan3: integer >= 1 → integer
#   {SukuKelipatan3(n) mengembalikan suku ke-n dari deret 3, 6, 9, 12, 15, 18, ...}

# Realisasi
def SukuKelipatan3(n):
    if n == 1:
        return 3
    else:
        return SukuKelipatan3(n - 1) + 3

# Aplikasi
print(SukuKelipatan3(1))    # 3
print(SukuKelipatan3(6))    # 18
print(SukuKelipatan3(10))   # 30