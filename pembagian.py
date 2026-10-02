# Nama File: pembagian.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Membagi dua bilangan (hasil bagi bulat) secara rekursif

# Definisi dan Spesifikasi
# Bagi: integer >= 0, integer > 0 → integer
#   {Bagi(A, B) mengembalikan hasil bagi bulat A dibagi B secara rekursif.}

# Realisasi
def Bagi(A, B):
    if A < B:
        return 0
    else:
        return 1 + Bagi(A - B, B)

# Aplikasi
print(Bagi(17, 5))      # 3
print(Bagi(3, 5))       # 0
print(Bagi(20, 4))      # 5