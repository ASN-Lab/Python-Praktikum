# Loops

# menggunakan range
range(5)

tahun = [2005,2021,2024]
N = len(tahun)

for i in range(N):
    print(tahun[i] , "\n")

# contoh loop

for i in range(-5,5):
    print(i, "\n")

# Loop mengurutkan data

for year in tahun:
    print(year, "\n")

# penggunaan Loop untuk mengganti element di dalam list

kotak = ['merah', 'kuning', 'hijau', 'ungu', 'biru']

for i in range(0, 5):
    print("Sebelum bangun datar persegi ", i, 'adalah',  kotak[i])
    kotak[i] = 'massa'
    print("Setelah bangun datar persegi ", i, 'adalah',  kotak[i], "\n")

# Loop untuk pengurutan dan pengisian data pada list

lingkaran=['merah', 'kuning', 'hijau', 'ungu', 'biru']

for i, bundaran in enumerate(lingkaran):
    print(i, bundaran, "\n")

# While Loop

masa = [1982, 1980, 1973, 2000]

i = 0
tahun = 0

while(tahun != 1973):
    tahun = masa[i]
    i = i + 1
    print(tahun)

print("Butuh", i ,"pengulangan untuk keluar dari Loop.\n")

# Nested Loop

# loop bagian luar
for i in range(1, 11):
    # nested loop
    # untuk setiap nilai i, loop ini akan dijalankan sebanyak 10 kali
    for j in range(1, 11):
        # print perkalian
        print(i * j, end=' ')
    print( "", "\n")

# while Loop di dalam for Loop

quotes = ['Jangan', 'Pernah', 'Menyerah']
# loop bagian luar
for name in quotes:
    # bagian dalam while loop
    count = 0
    while count < 1000:
        print(name, end=' ')
        # penghitung increment
        count = count + 1
    print("", "\n")

# Jeda pada nested Loop

for i in range(4):
    for j in range(4):
        if j == i:
            break
        print(i, j, "\n")

# nested Loop yang berlanjut

pt1 = [2, 4, 6]
pt2 = [2, 4, 6]
for i in pt1:
    for j in pt2:
        if i == j:
            continue
        print(i, '+', j, '= ', i + j)
        print(i, '-', j, '= ', i - j)
        print(i, '*', j, '= ', i * j)
        print(i, '/',  j, '= ', i / j, "\n")

# Nested While Loop

i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(j, end='')
        j = j + 1
    i = i + 1
    print("\n")

# For Loop di dalam While Loop

print('Angka sempurna antara 1 sampai 100:')
n = 2
# hile loop bagian luar
while n <= 100:
    x_sum = 0
    # bagian dalam for loop
    for i in range(1, n):
        if n % i == 0:
            x_sum += i
    if x_sum == n:
        print('Angka sempurna:', n, "\n")
    n += 1

# Quiz 1
for i in range(5, 10):
    print(i, "\n")

# Quiz 2
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for genre in Genres:
    print("-Genre lagu", genre, "\n")

# Quiz 3
squares=['merah', 'kuning', 'hijau', 'ungu', 'biru']

for square in squares:
    print("-Persegi warna", square, "\n")

# Exercise 1
print("membuat segitiga bintang")
n = int(input("Masukkan angka: "))

for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))

# Exercise 2
print("membuat segitiga pascal")
n = int(input("Masukkan angka: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        if k == 0 or k == i:
            print("1", end=" ")
        else:
            print(k, end=" ")
    print()

# Exercise 3
print("membuat segitiga pascal dan penjumlahan semua nilai baris")
n = int(input("Masukkan angka: "))

for i in range(n):
    sum = 0
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        if k == 0 or k == i:
            print("1", end=" ")
            sum += 1
        else:
            print(k, end=" ")
            sum += k
    print()
    print("Jumlah angka dalam satu baris segitiga pascal adalah: ", sum)