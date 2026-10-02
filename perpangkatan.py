# Nama File: perpangkatan.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 2 Oktober 2026
# Deskripsi: Memangkatkan bilangan secara rekursif

# Definisi dan Spesifikasi
# Pangkat: integer, integer >= 0 → integer
#   {Pangkat(A, N) mengembalikan A dipangkatkan N secara rekursif.}

# Realisasi
def Pangkat(A, N):
    if N == 0:
        return 1
    else:
        return A * Pangkat(A, N - 1)

# Aplikasi
print(Pangkat(2, 10))   # 1024
print(Pangkat(5, 0))    # 1
print(Pangkat(-3, 3))   # -27