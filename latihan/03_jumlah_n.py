def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Nilai n dimasukkan saat program dijalankan
n_input = int(input("Masukkan nilai n: "))
print(f"Jumlah 1 sampai {n_input} ->", jumlah_n(n_input))