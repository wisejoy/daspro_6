# Nama File : deret_suku_ke_n.py
# Pembuat : Bintang Fitra Wisesha
# Tanggal : 2 Oktober 2026
# Deskripsi : Menentukan bilangan ke-n dari sebuah deret secara rekursif

# Definisi dan Spesifikasi
# Deret1: integer >= 1 → integer
#   {Deret1(n) mengembalikan suku ke-n dari deret 3, 6, 9, 12, 15, 18, ...}

# Deret2: integer >= 1 → integer
#   {Deret2(n) mengembalikan suku ke-n dari deret 1, -2, 3, -4, 5, -6, ...}

# Realisasi
def Deret1(n):
    if n == 1:
        return 3
    else:
        return Deret1(n - 1) + 3



def Deret2(n):
    if n == 1:
        return 1
    elif n == 2:
        return -2
    elif n % 2 == 1:
        return Deret2(n - 2) + 2
    else:
        return Deret2(n - 2) - 2


# Aplikasi
print(Deret1(1))    # 3
print(Deret1(6))    # 18
print(Deret2(1))    # 1
print(Deret2(4))    # -4