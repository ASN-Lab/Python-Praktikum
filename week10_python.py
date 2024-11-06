import colorama
from colorama import Fore, Style, init

init()

print(Style.BRIGHT, "Week 10-Fungsi di dalam Python", Style.RESET_ALL, "\n")

# Membuat dan Memanggil sebuah function
def fungsi1(nama):
    print("Halo " + nama + ", ini adalah hasil dari membuat dan memanggil senuah fungsi!")

fungsi1("semuanya")

# Exercise 1
print(Style.BRIGHT + Fore.GREEN, "Exercise 1" + "\n" + Style.NORMAL + "Membuat program untuk menghitung nilai faktorial dari bilangan yang diinputkan dengan memanfaatkan fungsi rekrusif" + Style.RESET_ALL, "\n")

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

