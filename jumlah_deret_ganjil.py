# Nama File: jumlah_deret_ganjil.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Menjumlahkan deret 1 + 3 + 5 + 7 + 9 + 11 ... sampai suku ke-n

# Definisi dan Spesifikasi
# JumlahGanjil: integer >= 0 → integer
#   {JumlahGanjil(n) mengembalikan hasil 1 + 3 + 5 + 7 + ... sampai suku ke-n.}

# Realisasi
def JumlahGanjil(n):
    if n == 0:
        return 0
    else:
        return JumlahGanjil(n - 1) + (2 * n - 1)

# Aplikasi
print(JumlahGanjil(0))    # 0
print(JumlahGanjil(1))    # 1
print(JumlahGanjil(5))    # 25
print(JumlahGanjil(6))    # 36