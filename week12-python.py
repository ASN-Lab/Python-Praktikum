import matematika

print("<-------------------------------------------------------------------------------- Week 12-Python Python Try Except ------------------------------------------------------------->")
print("""
Python Try Except

Python try except adalah sebuah statement yang digunakan untuk menangani kesalahan atau exception yang terjadi dalam program. Statement ini terdiri dari dua bagian, yaitu try dan except.

Try
Statement try digunakan untuk menentukan blok kode yang ingin dijalankan. Jika terjadi kesalahan dalam blok kode ini, maka program akan mengeksekusi statement except.

Except
Statement except digunakan untuk menentukan blok kode yang ingin dijalankan jika terjadi kesalahan dalam blok kode try. Statement except dapat menangani kesalahan yang spesifik atau kesalahan yang umum.

Contoh Penggunaan Try Except
try:
    # Blok kode yang ingin dijalankan
    x = 5 / 0
except ZeroDivisionError:
    # Blok kode yang ingin dijalankan jika terjadi kesalahan
    print("Tidak bisa membagi dengan nol")

Penggunaan Try Except dengan Multiple Except
try:
    # Blok kode yang ingin dijalankan
    x = 5 / 0
except ZeroDivisionError:
    # Blok kode yang ingin dijalankan jika terjadi kesalahan ZeroDivisionError
    print("Tidak bisa membagi dengan nol")
except TypeError:
    # Blok kode yang ingin dijalankan jika terjadi kesalahan TypeError
    print("Tipe data tidak sesuai")

Penggunaan Try Except dengan Finally
try:
    # Blok kode yang ingin dijalankan
    x = 5 / 0
except ZeroDivisionError:
    # Blok kode yang ingin dijalankan jika terjadi kesalahan
    print("Tidak bisa membagi dengan nol")
finally:
    # Blok kode yang ingin dijalankan setelah try dan except
    print("Program selesai dijalankan")

Penggunaan Try Except dengan Raise
try:
    # Blok kode yang ingin dijalankan
    x = 5 / 0
    if x < 0:
        raise ValueError("Nilai tidak boleh negatif")
except ZeroDivisionError:
    # Blok kode yang ingin dijalankan jika terjadi kesalahan
    print("Tidak bisa membagi dengan nol")
except ValueError as e:
    # Blok kode yang ingin dijalankan jika terjadi kesalahan
    print(e)
""")

# Weekly Exercise
print("<-------------------------------------------------------------------------------- Weekly Exercise ------------------------------------------------------------------------------->")

# Weekly Exercise 1
print( "Weekly Exercise 1:\n")
print("Program penghitungan bangun datar menggunakan Exception Handling:" + "\n")

while True:
    try:
        print("Pilih bangun datar yang ingin dihitung:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        print("4. Segitiga")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
        if pilihan == "1":
            sisi = input("-Masukkan sisi persegi : ")
            if sisi == "":
                raise ValueError("Input tidak boleh kosong")
            sisi = int(sisi)
            print("Luas Persegi :", matematika.Matematika.luas_persegi(sisi))
        elif pilihan == "2":
            panjang = input("Masukkan nilai panjang: ")
            lebar = input("Masukkan nilai lebar: ")
            if panjang == "" or lebar == "":
                raise ValueError("Input tidak boleh kosong")
            panjang = int(panjang)
            lebar = int(lebar)
            hasil = matematika.persegi_panjang(panjang, lebar)
            print("Luas persegi panjang: ", hasil)
        elif pilihan == "3":
            jari_jari = input("Masukkan nilai jari-jari: ")
            if jari_jari == "":
                raise ValueError("Input tidak boleh kosong")
            jari_jari = int(jari_jari)
            hasil = matematika.lingkaran(jari_jari)
            print("Luas lingkaran: ", hasil)
        elif pilihan == "4":
            alas = input("Masukkan nilai alas: ")
            tinggi = input("Masukkan nilai tinggi: ")
            if alas == "" or tinggi == "":
                raise ValueError("Input tidak boleh kosong")
            alas = int(alas)
            tinggi = int(tinggi)
            hasil = matematika.segitiga(alas, tinggi)
            print("Luas segitiga: ", hasil)
        else:
            print("Pilihan tidak valid")
        break
    except ValueError as e:
        if e.args[0] == "Input tidak boleh kosong":
            print("Maaf, input tidak boleh kosong")
        else:
            print("Maaf, input harus berupa angka")

# Weekly Exercise 2
print( "Weekly Exercise 2:\n")
print("Modifikasi program UTS menggunakan Exception Handling:" + "\n")

# Soal 1

# judul program
print("Pendeteksi jumlah bilangan ganjil dan genap pada NPM\n")  

# Buat fungsi untuk menghitung jumlah bilangan ganjil dan genap dalam NPM
def jumlah_bilangan(npm):
    # Inisialisasi untuk bilangan ganjil dan genap
    bilangan_ganjil = 0 
    bilangan_genap = 0

    # Pengulangan instruksi setiap angka dalam NPM
    for angka in str(npm):
        # Cek apakah angka tersebut genap 
        if int(angka) % 2 == 0:
            # Jika genap, tambahkan ke variabel bilangan_genap
            bilangan_genap += 1
        else:
            # Jika ganjil, tambahkan ke variabel ganjil bilangan_ganjil
            bilangan_ganjil += 1
    # Mengembalikan hasil hitungan bilangan ganjil dan genap
    return bilangan_ganjil, bilangan_genap

# Menginputkan data berupa NPM
while True:
    try:
        npm = int(input("Masukkan NPM anda: "))
        break  # keluar dari loop jika input valid
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

# Memanggil fungsi untuk menghitung bilangan ganjil dan genap
ganjil, genap = jumlah_bilangan(npm)
# Cetak hasil
print(f"Jumlah bilangan ganjil adalah: {ganjil}")
print(f"Jumlah bilangan genap adalah: {genap}")

# Soal 2
# judul program
print("Segitiga Angka dan Jumlah Kelipatan Tiap Baris")

# Menginputkan jumlah baris dari segitiga angka
while True:
    try:
        segitiga_angka = int(input("Jumlah baris: "))
        if segitiga_angka <= 0:
            raise ValueError("Jumlah baris harus lebih besar dari 0.")
        break  # keluar dari loop jika input valid
    except ValueError as e:
        print(f"Input tidak valid: {e}. Harap masukkan angka positif.")

# Pengulangan setiap baris
for i in range(1, segitiga_angka + 1):
    # Pengulangan setiap kolom dalam baris
    for j in range(1, i + 1):
        # Cetak hasil perkalian baris dan kolom
        print(j * i, end=" ")
    # Pindah ke baris berikutnya setelah setiap baris
    print()