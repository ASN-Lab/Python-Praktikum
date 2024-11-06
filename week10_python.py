import colorama
from colorama import Fore, Style, init

init()

print(Style.BRIGHT + Fore.GREEN + "<--------------------------------------------------------------------------Week 10-Fungsi di dalam Python------------------------------------------------------------------------>" + Style.RESET_ALL + "\n")

# Membuat dan Memanggil sebuah function
print(Style.BRIGHT + Fore.GREEN + "Membuat dan Memanggil sebuah fungsi"  + Style.RESET_ALL)
print(Style.BRIGHT + "\nContoh membuat dan memanggil sebuah fungsi:" + Style.RESET_ALL)
print("""
        def fungsi1(nama):
            print("Halo " + nama + ", ini adalah hasil dari membuat dan memanggil senuah fungsi!")

        fungsi1("semuanya")
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def fungsi1(nama):
    print("Halo " + nama + ", ini adalah hasil dari membuat dan memanggil senuah fungsi!")

fungsi1("semuanya")

# Argument
print("\n" + Style.BRIGHT + Fore.GREEN + "Argument" + Style.RESET_ALL + "\n")
print("Argument adalah sebuah nilai yang dikirimkan ke dalam sebuah fungsi.\n")
print(Style.BRIGHT + "Contoh argument:" + Style.RESET_ALL)
print("""
        def fungsi2(nama_depan):
            print("-" + nama_depan + " Potter")

        fungsi2("Harry")
        fungsi2("James")
        fungsi2("Lilly")
""")
print(Style.BRIGHT + "Output:" + Style.RESET_ALL)

def fungsi2(nama_depan):
    print("-" + nama_depan + " Potter")

fungsi2("Harry")
fungsi2("James")
fungsi2("Lilly")

# Parameter dan argument
print("\n" + Style.BRIGHT + Fore.GREEN + "Perbedaan parameter dan argument" + Style.RESET_ALL + "\n")
print(Style.BRIGHT + "Parameter:" + "\n" + Style.RESET_ALL, "Variabel yang digunakan untuk menerima argument.\n")
print(Style.BRIGHT + "Argument:" + "\n" + Style.RESET_ALL, "Nilai yang dikirimkan ke dalam sebuah fungsi untuk diproses lebih lanjut.")

# Angka dari argument
print("\n" + Style.BRIGHT + Fore.GREEN + "Angka dari argument" + Style.RESET_ALL + "\n")
print("Angka dari argument adalah jumlah argument yang dapat diterima oleh sebuah fungsi.")
print("Contoh penggunaan angka dari argument:")
print("""
        def fungsi3(namadepan, namabelakang):
            print(namadepan + " " + namabelakang)

        fungsi3("Harry", "Potter")
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def fungsi3(namadepan, namabelakang):
    print(namadepan + " " + namabelakang)

fungsi3("Harry", "Potter")
print("\n" + Style.BRIGHT + "Penjelasan:" + "\n" + Style.NORMAL + "Untuk fungsi yang dipanggil di atas, kita hanya membuat 2 buah argument, maka fungsi hanya akan dapat menampilkan 2 buah argument, jika kita memanggil fungsi tersebut dengan jumlah argumentnya lebih dari 2 maka akan terjadi error." + Style.RESET_ALL + "\n")

print(Style.BRIGHT + "Contoh pemanggilan fungsi yang melebih dari jumlah argument yang dibuat:" + Style.RESET_ALL)
print("""
        def fungsi3(namadepan, namabelakang):
            print(namadepan + " " + namaTengah + namabelakang)

        fungsi3("Harry", "Potter")
""")

print(Style.BRIGHT + "Output:\n" + Style.RESET_ALL, Fore.RED + "NameError: name 'namaTengah' is not defined" + Style.RESET_ALL)

# Argumen Arbitrary
print("\n" + Style.BRIGHT + Fore.GREEN + "Argumen Arbitrary" + Style.RESET_ALL + "\n")
print("Argumen arbitrary adalah argumen yang dapat menerima jumlah argumen yang tidak terbatas.\n")
print(Style.BRIGHT + "Contoh argumen arbitrary:" + Style.RESET_ALL)
print("""
        def fungsi4(*args):
            for arg in args:
                print("-" + arg)

        fungsi4("Harry", "Potter", "James", "Lilly")
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def fungsi4(*args):
    for arg in args:
        print("-" + arg)

fungsi4("Harry", "Potter", "James", "Lilly")

print("\n" + Style.BRIGHT + "Penjelasan:" + "\n" + Style.NORMAL + "Pada contoh di atas, kita menggunakan tanda", Style.BRIGHT + Fore.CYAN + "*args" + Style.RESET_ALL, "untuk menandakan bahwa fungsi tersebut dapat menerima jumlah argumen yang tidak terbatas. Kemudian, kita menggunakan perulangan for untuk menampilkan semua argumen yang diterima oleh fungsi tersebut." + Style.RESET_ALL + "\n")

# Keyword Argument
print("\n" + Style.BRIGHT + Fore.GREEN + "Keyword Argument" + Style.RESET_ALL + "\n")
print("Keyword argument adalah argumen yang dapat diberikan nilai dengan menggunakan nama parameter.\n")
print(Style.BRIGHT + "Contoh keyword argument:" + Style.RESET_ALL)
print("""
        def fungsi5(nama_depan, nama_belakang):
            print(nama_depan + " " + nama_belakang)

        fungsi5(nama_belakang="Potter", nama_depan="Harry")
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def fungsi5(nama_depan, nama_belakang):
    print(nama_depan + " " + nama_belakang)

fungsi5(nama_belakang="Potter", nama_depan="Harry")

print("\n" + Style.BRIGHT + "Penjelasan:" + "\n" + Style.NORMAL + "Pada contoh di atas, kita menggunakan keyword argument untuk memberikan nilai pada parameter nama_depan dan nama_belakang. Dengan menggunakan keyword argument, kita dapat mengatur urutan parameter sesuai dengan kebutuhan." + Style.RESET_ALL + "\n")

# Argumen Kata Kunci Arbitrary
print("\n" + Style.BRIGHT + Fore.GREEN + "Arbitrary Keyword Argument" + Style.RESET_ALL + "\n")
print("Argumen kata kunci arbitrary adalah argumen yang dapat menerima jumlah argumen kata kunci yang tidak terbatas. Argumen kata kunci arbitrary ditandai dengan", Style.BRIGHT + Fore.CYAN + "**kwargs.\n" + Style.RESET_ALL)

# Contoh Argumen Kata Kunci Arbitrary
print(Style.BRIGHT + "Contoh fungsi dari argumen kata kunci arbitrary:" + Style.RESET_ALL)

print("""
        def fungsi6(**kwargs):
            for key, value in kwargs.items():
                print(f"-{key}: {value}")

        fungsi6(nama="Harry", umur=20, kota="Jakarta")
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def fungsi6(**kwargs):
    for key, value in kwargs.items():
        print(f"-{key}: {value}")

fungsi6(nama="Harry", umur=20, kota="Jakarta")

# Penjelasan
print("\n" + Style.BRIGHT + "Penjelasan:" + Style.RESET_ALL)
print("Pada contoh di atas, kita menggunakan **kwargs untuk menandakan bahwa fungsi tersebut dapat menerima jumlah argumen kata kunci yang tidak terbatas. Kemudian, kita menggunakan perulangan", Fore.MAGENTA + "for" + Style.RESET_ALL , "untuk menampilkan semua argumen kata kunci yang diterima oleh fungsi tersebut.\n")

# Manfaat Argumen Kata Kunci Arbitrary
print(Style.BRIGHT + "Manfaat penggunaan argumen:" + Style.RESET_ALL)
print("Argumen kata kunci arbitrary sangat berguna ketika kita tidak tahu berapa banyak argumen yang akan diterima oleh sebuah fungsi. Dengan menggunakan argumen kata kunci arbitrary, kita dapat membuat fungsi yang lebih fleksibel dan dapat menangani berbagai macam kasus.\n")

# Contoh Penggunaan Argumen Kata Kunci Arbitrary
print(Style.BRIGHT + "Contoh Penggunaan Argumen:" + Style.RESET_ALL)
print("""
        def buat_profil(**kwargs):
            profil = {}
            for key, value in kwargs.items():
                profil[key] = value
            return profil

        profil = buat_profil(nama="Harry", umur=20, kota="Jakarta", pekerjaan="Mahasiswa")
        print(profil)
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def buat_profil(**kwargs):
    profil = {}
    for key, value in kwargs.items():
        profil[key] = value
    return profil

profil = buat_profil(nama="Harry", umur=20, kota="Jakarta", pekerjaan="Mahasiswa")

print(profil)

print("\n" + Style.BRIGHT + "Penjelasan:" + Style.RESET_ALL)
print("Pada contoh di atas, kita menggunakan argumen kata kunci arbitrary untuk membuat sebuah fungsi yang dapat membuat profil seseorang. Fungsi tersebut dapat menerima berbagai macam argumen kata kunci, seperti nama, umur, kota, pekerjaan, dan lain-lain.\n")

# Default Parameter Value
print("\n" + Style.BRIGHT + Fore.GREEN + "Default Parameter Value" + Style.RESET_ALL + "\n")
print("Default parameter value adalah nilai yang diberikan kepada parameter jika tidak ada nilai yang diberikan saat memanggil fungsi.\n")
print(Style.BRIGHT + "Contoh default parameter value:" + Style.RESET_ALL)
print(""" 
        def fungsi7(nama, umur=20):
            print("Nama: " + nama)
            print("Umur: " + str(umur))

        fungsi7("Harry")
        fungsi7("James", 25)
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def fungsi7(nama, umur=20):
    print("Nama: " + nama)
    print("Umur: " + str(umur) + "\n")

fungsi7("Harry")
fungsi7("James", 25)

print("\n" + Style.BRIGHT + "Penjelasan:" + Style.RESET_ALL)
print("Pada contoh di atas, kita menggunakan default parameter value untuk memberikan nilai umur 20 jika tidak ada nilai yang diberikan saat memanggil fungsi.")

# Passing List sebagai Argumen
print("\n" + Style.BRIGHT + Fore.GREEN + "Passing List sebagai Argumen" + Style.RESET_ALL + "\n")
print("List dapat dilewatkan sebagai argumen ke dalam sebuah fungsi.\n")
print(Style.BRIGHT + "Contoh passing list sebagai argumen:" + Style.RESET_ALL)
print("""
        def tampilkan_daftar(daftar):
            for item in daftar:
                print(item)

        daftar_buah = ["Apel", "Banana", "Ceri"]
        tampilkan_daftar(daftar_buah)
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def tampilkan_daftar(daftar):
    for item in daftar:
        print(item)

daftar_buah = ["Apel", "Banana", "Ceri"]
tampilkan_daftar(daftar_buah)

print("\n" + Style.BRIGHT + "Penjelasan:" + Style.RESET_ALL)
print("Pada contoh di atas, kita membuat sebuah fungsi tampilkan_daftar() yang menerima sebuah list sebagai argumen. Kemudian, kita membuat sebuah list daftar_buah dan melewatinya sebagai argumen ke dalam fungsi tampilkan_daftar().")

# Nilai Kembali (Return Values)
print("\n" + Style.BRIGHT + Fore.GREEN + "Nilai Kembali (Return Values)" + Style.RESET_ALL)
print("Nilai kembali adalah nilai yang dikembalikan oleh sebuah fungsi setelah proses eksekusi selesai.\n")
print(Style.BRIGHT + "Contoh penggunaan nilai kembali:" + Style.RESET_ALL)
print("""
        def tambah(x, y):
            return x + y

        hasil = tambah(5, 3)
        print("Hasil:", hasil)
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def tambah(x, y):
    return x + y

hasil = tambah(5, 3)
print("Hasil:", hasil)

print("\n" + Style.BRIGHT + "Penjelasan:" + Style.RESET_ALL)
print("Pada contoh di atas, kita membuat sebuah fungsi tambah() yang menerima dua argumen x dan y. Fungsi tersebut kemudian mengembalikan nilai hasil penjumlahan x dan y menggunakan pernyataan return. Nilai kembali tersebut kemudian disimpan dalam variabel hasil dan dicetak ke layar.")

# Pass Statement
print("\n" + Style.BRIGHT + Fore.GREEN + "Pass Statement" + Style.RESET_ALL)
print("Pass statement adalah pernyataan yang digunakan dalam bahasa pemrograman Python untuk menunjukkan bahwa sebuah blok kode tidak memiliki pernyataan yang dapat dijalankan. Pass statement sering digunakan sebagai placeholder ketika kita ingin menulis kode yang belum selesai atau ketika kita ingin membuat sebuah blok kode yang tidak memiliki pernyataan yang dapat dijalankan.\n")

# Contoh Penggunaan Pass Statement
print(Style.BRIGHT + "Contoh Pass Statement:" + Style.RESET_ALL)
print("""
        def fungsi_kosong():
            pass

        fungsi_kosong()
""")

def fungsi_kosong():
    pass

fungsi_kosong()

print(Style.BRIGHT + "Penjelasan:" + Style.RESET_ALL)
print("Pada contoh di atas, kita membuat sebuah fungsi kosong yang tidak memiliki pernyataan yang dapat dijalankan. Kita menggunakan pass statement untuk menunjukkan bahwa fungsi tersebut tidak memiliki pernyataan yang dapat dijalankan.\n")

# Penggunaan Pass Statement dalam Struktur Kontrol
print(Style.BRIGHT + "Penggunaan Pass Statement dalam Struktur Kontrol" + Style.RESET_ALL)
print("Pass statement juga dapat digunakan dalam struktur kontrol seperti", Fore.MAGENTA + "if elif else for" + Style.RESET_ALL, "dan", Fore.MAGENTA + "while" + Style.RESET_ALL,". Berikut adalah contoh penggunaan pass statement dalam struktur kontrol:")
print("""
        x = 5
        if x > 10:
            pass
        else:
            print("x kurang dari atau sama dengan 10")
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
x = 5
if x > 10:
    pass
else:
    print("x kurang dari atau sama dengan 10")

print("\n" + Style.BRIGHT + "Penjelasan:" + Style.RESET_ALL)
print("Pada contoh di atas, kita menggunakan pass statement dalam struktur kontrol", Fore.MAGENTA + "if-else" + Style.RESET_ALL, ". Jika x lebih besar dari 10, maka tidak ada pernyataan yang dijalankan. Jika x kurang dari atau sama dengan 10, maka pernyataan print akan dijalankan.\n")

# Penggunaan Pass Statement dalam Kelas
print(Style.BRIGHT + "Penggunaan Pass Statement dalam Sebuah Kelas:" + Style.RESET_ALL)
("Pass statement juga dapat digunakan dalam kelas untuk menunjukkan bahwa sebuah metode atau atribut tidak memiliki implementasi. Berikut adalah contoh penggunaan pass statement dalam kelas:")
print("""
        class KelasKosong:
            def metode_kosong(self):
                pass

        objek = KelasKosong()
        objek.metode_kosong()
""")
class KelasKosong:
    def metode_kosong(self):
        pass

objek = KelasKosong()
objek.metode_kosong()

print(Style.BRIGHT + "Penjelasan:" + Style.RESET_ALL)
print("Pada contoh di atas, kita membuat sebuah kelas kosong yang memiliki metode kosong. Kita menggunakan pass statement untuk menunjukkan bahwa metode tersebut tidak memiliki implementasi.\n")

# Rekursi dalam Bahasa Pemrograman Python
print(Style.BRIGHT + Fore.GREEN + "Rekursi" + Style.RESET_ALL)
print("Rekursi adalah sebuah teknik pemrograman yang memungkinkan sebuah fungsi untuk memanggil dirinya sendiri. Teknik ini sering digunakan untuk menyelesaikan masalah yang memiliki pola yang sama dan dapat dipecah menjadi sub-masalah yang lebih kecil.\n")

# Contoh Rekursi
print(Style.BRIGHT + "Contoh Rekursi" + Style.RESET_ALL)
print("Contoh sederhana dari rekursi adalah fungsi yang menghitung nilai faktorial dari sebuah bilangan. Faktorial dari sebuah bilangan adalah hasil perkalian dari bilangan tersebut dengan semua bilangan positif yang lebih kecil darinya.\n")

# Fungsi Rekursi untuk Menghitung Faktorial
print(Style.BRIGHT + "Fungsi Rekursi untuk Menghitung Faktorial" + Style.RESET_ALL)
print(""" 
        def faktorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * faktorial(n-1)
""")

# Contoh Penggunaan Fungsi Rekursi
print(Style.BRIGHT + "Contoh Penggunaan" + Style.RESET_ALL)
print("Contoh penggunaan fungsi rekursi untuk menghitung nilai faktorial dari bilangan 5:\n")
print("faktorial(5) = 5 * faktorial(4)")
print("faktorial(4) = 4 * faktorial(3)")
print("faktorial(3) = 3 * faktorial(2)")
print("faktorial(2) = 2 * faktorial(1)")
print("faktorial(1) = 1\n")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
print("faktorial(5) = 5 * 4 * 3 * 2 * 1 = 120\n")

# Implementasi Fungsi Rekursi dalam Bahasa Pemrograman Python
print(Style.BRIGHT + "Implementasi Fungsi Rekursi dalam Bahasa Pemrograman Python" + Style.RESET_ALL)
print("""
        def faktorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * faktorial(n-1)

        bilangan = 5
        print("Faktorial dari", bilangan, "adalah:", faktorial(bilangan))
""")

print(Style.BRIGHT + "Output:" + Style.RESET_ALL)
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

bilangan = 5
print("Faktorial dari", bilangan, "adalah:", faktorial(bilangan))

# Exercise
print("\n" + Style.BRIGHT + Fore.GREEN + "<------------------------------------------------------------------------------------Exercise------------------------------------------------------------------------------------>" + Style.RESET_ALL + "\n")

# Exercise 1
print(Style.BRIGHT + Fore.GREEN + "Exercise 1")
print(Style.NORMAL + Fore.GREEN + "Membuat program untuk menghitung nilai faktorial dari bilangan yang diinputkan dengan memanfaatkan fungsi rekrusif" + Style.RESET_ALL)

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

bilangan = int(input("Masukkan bilangan: "))
print("Faktorial dari", bilangan, "adalah:", faktorial(bilangan), "\n")

# Exercise 2
print(Style.BRIGHT + Fore.GREEN, "Exercise 2" + "\n" + Style.NORMAL + "Membuat program kalkulator untuk menghitung luas bangun datar lingkaran, persegi, dan segitiga" + Style.RESET_ALL, "\n")

def hitung_luas_lingkaran():
    phi = 3.14
    r = float(input("Masukkan jari-jari lingkaran: "))
    luas = phi * r * r
    print("Luas lingkaran adalah: ", luas)

def hitung_luas_persegi():
    s = float(input("Masukkan sisi persegi: "))
    luas = s * s
    print("Luas persegi adalah: ", luas)

def hitung_luas_segitiga():
    a = float(input("Masukkan alas segitiga: "))
    t = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * a * t
    print("Luas segitiga adalah: ", luas)

def main():
    while True:
        print("Pilih perhitungan:")
        print("1. Luas Lingkaran")
        print("2. Luas Persegi")
        print("3. Luas Segitiga")
        print("4. Selesai\n")
        pilihan = input("Masukkan pilihan: \n")
        if pilihan == "1":
            hitung_luas_lingkaran()
        elif pilihan == "2":
            hitung_luas_persegi()
        elif pilihan == "3":
            hitung_luas_segitiga()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()

