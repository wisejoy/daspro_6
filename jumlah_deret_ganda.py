# Nama File: jumlah_deret_ganda.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Menjumlahkan deret 1 + 2 + 4 + 8 + 16 + 32 ... sampai suku ke-n

# Definisi dan Spesifikasi
# JumlahGanda: integer >= 0 → integer
#   {JumlahGanda(n) mengembalikan hasil 1 + 2 + 4 + 8 + ... sampai suku ke-n.}

# Realisasi
def JumlahGanda(n):
    if n == 0:
        return 0
    else:
        return 1 + 2 * JumlahGanda(n - 1)

# Aplikasi
print(JumlahGanda(0))     # 0
print(JumlahGanda(1))     # 1
print(JumlahGanda(4))     # 15
print(JumlahGanda(6))     # 63