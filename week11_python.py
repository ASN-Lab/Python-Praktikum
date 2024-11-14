import colorama
import module1
import matematika
from colorama import Fore, Style, init

init()

print(Style.BRIGHT + Fore.GREEN + "<--------------------------------------------------------------------------------------------- Week 11-Module di dalam Python -------------------------------------------------------------------------->" + Style.RESET_ALL + "\n")

# Membuat sebuah modul
print(Fore.GREEN + "1. Membuat Modul" + Style.RESET_ALL + "\n" + "Untuk membuat sebuah modul, kita dapat dengan membuat sebuah file sebagai modul yang berekstensikan", Fore.MAGENTA + ".py" + Style.RESET_ALL + ".", Style.BRIGHT + "\n\nContoh:")
print("Nama module :" + Style.RESET_ALL, "module1.py", Style.BRIGHT + "\nIsi module :" + Style.RESET_ALL, "\n" + """
def perkenalan(nama):
    print("Halo, " + nama)
""")

# Menggunakan modul
print(Fore.GREEN + "2. Menggunakan Module" + Style.RESET_ALL + "\n" + "Untuk menggunakan/memanggil modul yang sudah dibuat adalah dengan cara melakukan import dari modul tersebut.", Style.BRIGHT + "\n\nContoh:" + Style.RESET_ALL, """
import module1
module1.perkenalan("Aldi")
      """ + "\n" + Style.BRIGHT + "Output:" + Style.RESET_ALL)

module1.perkenalan("Aldi" + "\n")

# Variabel di dalam modul
print(Fore.GREEN + "3. Variabel" + Style.RESET_ALL)
print("Variabel di dalam modul dapat diakses dengan cara menggunakan nama modul dan nama variabel.", Style.BRIGHT + "\n\nContoh:" + Style.RESET_ALL, """
person1 = {
      "nama": "Aldi",
      "umur": "19",
      "asal": "Indonesia"
      }
      """, Style.BRIGHT, "\n" + "Kode program file utama:\n" + Style.RESET_ALL, """
import module1

a = module1.person1
print(a)

""" + Style.BRIGHT + "Output:" + Style.RESET_ALL)

a = module1.person1
print(a, "\n")

# Menamai modul
print(Fore.GREEN + "4. Menamai Modul" + Style.RESET_ALL + "\n" + "Dalam menamai file modul bisa sesuka yang kita mau, tetapi harus memiliki ekstensi file", Fore.MAGENTA + ".py" + Style.RESET_ALL + ".\n")

# Mengganti nama modul
print(Fore.GREEN + "5. Mengganti Nama Modul" + Style.RESET_ALL, "\n" + "Nama file modul dapat dibuat menjadi alias saat mengimpor modul, dengan menggunakan", Fore.MAGENTA + "as" + Style.RESET_ALL + ".\n\n" + Style.BRIGHT + "Contoh:" + Style.RESET_ALL + """
import module1 as m1
      
a = m1.person1
print(a)
""" + "\n" + Style.BRIGHT + "Output:" + Style.RESET_ALL)

import module1 as m1
      
a = m1.person1
print(a, "\n")

# Built-in Module
print(Fore.GREEN + "6. Built-in Module" + Style.RESET_ALL + "\n" + "Ada beberapa modul bawaan di Python, yang dapat digunakan kapan pun kita mau." + "\n\n" + Style.BRIGHT + "Contoh:" + Style.RESET_ALL + """
import platform
print(platform.system())
""", "\n" + Style.BRIGHT + "Output:" + Style.RESET_ALL)

import platform
print(platform.system(), "\n")

# Fungsi dir()
print(Fore.GREEN + "7. Fungsi dir()" + Style.RESET_ALL, "\n" + "Ada fungsi bawaan untuk mencantumkan semua nama fungsi (atau variabel nama) dalam modul, yaitu menggunakan fungsi" + Fore.MAGENTA + "dir()" + Style.RESET_ALL + ".\n\n" + Style.BRIGHT + "Contoh:" + Style.RESET_ALL, """
import platform
print(dir(platform))
""", "\n" + Style.BRIGHT + "Output:" + Style.RESET_ALL)
print(dir(platform), "\n\n" + Style.BRIGHT + "Catatan:" + Style.RESET_ALL + "\nFungsi dir() akan menampilkan semua nama fungsi, variabel, dan atribut yang ada dalam modul." + "\n")

# Import dari modul
print(Fore.GREEN + "8. Import dari Modul" + Style.RESET_ALL + "\n" + "Kita dapat memilih untuk mengimpor hanya bagian tertentu dari modul, dengan menggunakan", Fore.MAGENTA + "from" + Style.RESET_ALL + ".", "\n\n" + Style.BRIGHT + "Contoh:" + Style.RESET_ALL + """
def biodata(nama):
    print("Nama saya adalah " + nama["nama"])
    person1 = {
        "nama": "Aldi",
        "umur": "19",
        "asal": "Indonesia"
    }
""", "\n" + Style.BRIGHT + "Kode program file utama:\n" + Style.RESET_ALL, """
from module1 import person1
print(person1)
""", "\n" + Style.BRIGHT + "Output:" + Style.RESET_ALL)
from module1 import person1
print(person1, "\n" + Style.BRIGHT + "\nCatatan:" + Style.RESET_ALL + "\nSaat mengimpor menggunakan", Fore.MAGENTA + "from" + Style.RESET_ALL + ", jangan gunakan nama modul saat merujuk ke elemen dalam modul.\n")

# Weekly Exercise
print(Fore.GREEN + "<------------------------------------------------------------------------------------------- Weekly Exercise ------------------------------------------------------------------------------------------->" + Style.RESET_ALL)
print(Style.BRIGHT + "\nIsi Module matematika.py :\n" + Style.RESET_ALL + """
import math
import random
import statistics

class Matematika:
    PI = math.pi

    @staticmethod
    def luas_lingkaran(r):
        return Matematika.PI * r ** 2

    @staticmethod
    def luas_persegi(s):
        return s ** 2

    @staticmethod
    def keliling_lingkaran(r):
        return 2 * Matematika.PI * r

    @staticmethod
    def volume_kubus(s):
        return s ** 3

    @staticmethod
    def akar_kuadrat(x):
        return math.sqrt(x)

    @staticmethod
    def rata_rata(data):
        return statistics.mean(data)

    @staticmethod
    def bilangan_acak(min_value, max_value):
        return random.randint(min_value, max_value)
""")

print(Style.BRIGHT + "Exercise 1\nMelakukan import modul matematika.py dan menghitung luas dari lingkaran dan persegi" + Style.RESET_ALL + Fore.GREEN)

r = float(input("-Masukkan jari-jari lingkaran : "))
s = float(input("-Masukkan sisi persegi : "))

print(Fore.CYAN + "1. Konstanta Pi :", matematika.Matematika.PI)
print("2. Luas Lingkaran :", matematika.Matematika.luas_lingkaran(r))
print("3. Luas Persegi :", matematika.Matematika.luas_persegi(s))

# Exercise 2
print(Style.RESET_ALL + Style.BRIGHT + "\nExercise 2\nMelakukan import modul matematika.py dan memanggil 5 fungsi yang memanfaatkan built-in" + Style.RESET_ALL + Fore.GREEN)

x = float(input("-Masukkan bilangan untuk dihitung akar kuadratnya : "))
data = [float(input(f"-Masukkan angka ke-{i+1} untuk menghitung nilai rata-rata : ")) for i in range(5)]
min_value = int(input("-Masukkan nilai minimum untuk bilangan acak : "))
max_value = int(input("-Masukkan nilai maksimum untuk bilangan acak : "))
r = float(input("-Masukkan jari-jari lingkaran : "))
s = float(input("-Masukkan sisi kubus : "))

print(Fore.CYAN + "1. Akar Kuadrat :", matematika.Matematika.akar_kuadrat(x))
print("2. Rata-rata :", matematika.Matematika.rata_rata(data))
print("3. Bilangan Acak :", matematika.Matematika.bilangan_acak(min_value, max_value))
print("4. Keliling Lingkaran:", matematika.Matematika.keliling_lingkaran(r))
print("5. Volume Kubus :", matematika.Matematika.volume_kubus(s), Style.RESET_ALL)
