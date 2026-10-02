# Nama File: pengurangan.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Mengurangkan dua bilangan secara rekursif

# Definisi dan Spesifikasi
# Kurang: 2 integer → integer
#   {Kurang(A, B) mengurangkan bilangan A dengan bilangan B secara rekursif.}

# Realisasi
def Kurang(A, B):
    if B == 0:
        return A
    elif B > 0:
        return Kurang(A - 1, B - 1)
    else:
        return Kurang(A + 1, B + 1)

# Aplikasi
print(Kurang(10, 4))    # 6
print(Kurang(4, -7))    # 11
print(Kurang(-3, 5))    # -8