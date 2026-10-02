# Nama File: aritmatika_rekursif.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Operasi aritmatika (pengurangan, perkalian, pembagian,
#            perpangkatan) secara rekursif

# Definisi dan Spesifikasi

# Kurang: 2 integer → integer
#   {Kurang(A, B) mengurangkan bilangan A dengan bilangan B secara rekursif.}

# Kali: 2 integer → integer
#   {Kali(A, B) mengalikan bilangan A dengan bilangan B secara rekursif.}

# Bagi: integer >= 0, integer > 0 → integer
#   {Bagi(A, B) mengembalikan hasil bagi bulat A dibagi B secara rekursif.}

# Pangkat: integer, integer >= 0 → integer
#   {Pangkat(A, N) mengembalikan A dipangkatkan N secara rekursif.}

# Realisasi
def Kurang(A, B):
    if B == 0:
        return A
    elif B > 0:
        return Kurang(A - 1, B - 1)
    else:
        return Kurang(A + 1, B + 1)


def Kali(A, B):
    if B == 0:
        return 0
    elif B > 0:
        return A + Kali(A, B - 1)
    else:
        return Kali(A, B + 1) - A


def Bagi(A, B):
    if A < B:
        return 0
    else:
        return 1 + Bagi(A - B, B)


def Pangkat(A, N):
    if N == 0:
        return 1
    else:
        return A * Pangkat(A, N - 1)

# Aplikasi
print(Kurang(10, 4)) # 6
print(Kali(6, 7)) # 42
print(Bagi(17, 5)) # 3
print(Pangkat(2, 10)) # 1024