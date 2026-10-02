# Nama File: perkalian.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Mengalikan dua bilangan secara rekursif

# Definisi dan Spesifikasi
# Kali: 2 integer → integer
#   {Kali(A, B) mengalikan bilangan A dengan bilangan B secara rekursif.}

# Realisasi
def Kali(A, B):
    if B == 0:
        return 0
    elif B > 0:
        return A + Kali(A, B - 1)
    else:
        return Kali(A, B + 1) - A

# Aplikasi
print(Kali(6, 7))       # 42
print(Kali(6, -7))      # -42
print(Kali(0, 5))       # 0