# Nama File : deret_jumlah.py
# Pembuat : Bintang Fitra Wisesaha
# Tanggal : 2 Oktober 2026
# Deskripsi : Menentukan hasil penjumlahan deret sampai suku ke-n secara rekursif

# Definisi dan Spesifikasi
# JumlahGanjil : integer >= 0 → integer
#   {JumlahGanjil(n) mengembalikan hasil 1 + 3 + 5 + 7 + ... sampai suku ke-n.}
# JumlahGanda : integer >= 0 → integer
#   {JumlahGanda(n) mengembalikan hasil 1 + 2 + 4 + 8 + ... sampai suku ke-n.}

# Realisasi
def JumlahGanjil(n):
    if n == 0:
        return 0
    else:
        return JumlahGanjil(n - 1) + (2 * n - 1)

def JumlahGanda(n):
    if n == 0:
        return 0
    else:
        return 1 + 2 * JumlahGanda(n - 1)


# Aplikasi
print(JumlahGanjil(0))    # 0
print(JumlahGanjil(1))    # 1
print(JumlahGanjil(5))    # 25
print(JumlahGanjil(6))    # 36
print(JumlahGanda(0))     # 0
print(JumlahGanda(1))     # 1
print(JumlahGanda(4))     # 15
print(JumlahGanda(6))     # 63