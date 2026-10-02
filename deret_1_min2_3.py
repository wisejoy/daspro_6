1# Nama File: deret_1_min2_3.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Menentukan bilangan ke-n dari deret 1, -2, 3, -4, 5, -6, ...

# Definisi dan Spesifikasi
# SukuBergantian: integer >= 1 → integer
#   {SukuBergantian(n) mengembalikan suku ke-n dari deret 1, -2, 3, -4, 5, -6, ...}

# Realisasi
def SukuBergantian(n):
    if n == 1:
        return 1
    elif n % 2 == 1:
        return -SukuBergantian(n - 1) + 1
    else:
        return -SukuBergantian(n - 1) - 1

# Aplikasi
print(SukuBergantian(1))    # 1
print(SukuBergantian(4))    # -4
print(SukuBergantian(7))    # 7
print(SukuBergantian(10))   # -10