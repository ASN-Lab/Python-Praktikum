# Import Colorama
from colorama import Fore, Back, Style
import colorama

# Inisialisasi Colorama
colorama.init()

def print_header(text):
    print(f"\n{Back.BLUE}{Fore.WHITE} {text} {Style.RESET_ALL}")

def print_subheader(text):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{text}{Style.RESET_ALL}")

def print_example(text):
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")

def print_explanation(text):
    print(f"{Fore.CYAN}{text}{Style.RESET_ALL}")

# List
print_header("List")
print_explanation("List adalah struktur data yang mutable dan berurutan.")
print_explanation("Kegunaan: Menyimpan koleksi item yang dapat diubah dan diakses dengan indeks.")

my_list = [1, 2, 3, "apple", "banana"]
print_subheader("Contoh List:")
print_example(f"my_list = {my_list}")
print_example(f"Akses elemen: my_list[0] = {my_list[0]}")
print_example(f"Ubah elemen: my_list[1] = 'changed'")
my_list[1] = 'changed'
print_example(f"List setelah diubah: {my_list}")

# Tuple
print_header("Tuple")
print_explanation("Tuple adalah struktur data yang immutable dan berurutan.")
print_explanation("Kegunaan: Menyimpan koleksi item yang tidak boleh diubah setelah dibuat.")

my_tuple = (1, 2, 3, "apple", "banana")
print_subheader("Contoh Tuple:")
print_example(f"my_tuple = {my_tuple}")
print_example(f"Akses elemen: my_tuple[0] = {my_tuple[0]}")
print_example("Tuple tidak bisa diubah setelah dibuat")

# Set
print_header("Set")
print_explanation("Set adalah struktur data yang mutable, tidak berurutan, dan tidak memiliki duplikat.")
print_explanation("Kegunaan: Menyimpan koleksi item unik dan melakukan operasi himpunan.")

my_set = {1, 2, 3, "apple", "banana"}
print_subheader("Contoh Set:")
print_example(f"my_set = {my_set}")
print_example("Menambah elemen: my_set.add('orange')")
my_set.add('orange')
print_example(f"Set setelah ditambah: {my_set}")
print_example("Set otomatis menghilangkan duplikat")

# Dictionary
print_header("Dictionary")
print_explanation("Dictionary adalah struktur data yang mutable dengan pasangan key-value.")
print_explanation("Kegunaan: Menyimpan data dalam format key-value untuk akses cepat.")

my_dict = {"name": "John", "age": 30, "city": "New York"}
print_subheader("Contoh Dictionary:")
print_example(f"my_dict = {my_dict}")
print_example(f"Akses value: my_dict['name'] = {my_dict['name']}")
print_example("Menambah/mengubah elemen: my_dict['job'] = 'Engineer'")
my_dict['job'] = 'Engineer'
print_example(f"Dictionary setelah diubah: {my_dict}{Style.RESET_ALL}")

# Weekly Exercise
print(Style.BRIGHT + Fore.RED + "\nWeekly Exercise 1:" + "\n" +  Style.RESET_ALL)
print(Style.BRIGHT + Fore.GREEN + "Perbedaan list, tuple, set, dan dictionary:" + "\n" +  Style.RESET_ALL)

# List
print(Style.BRIGHT + Fore.YELLOW + "1. List:" + Style.RESET_ALL)
print(Fore.GREEN + " -Digunakan untuk menyimpan koleksi item yang berurutan.\n", "-Dapat diubah setelah dibuat.\n", "-Dibuat menggunakan tanda kurung siku [ ].\n", "-Memungkinkan duplikasi item.\n", "-Contoh: my_list = [1, 2, 3, 'a', 'b', 'c'].\n", "-Akses elemen menggunakan indeks: my_list[0].\n")

# Tuple
print(Style.BRIGHT + Fore.YELLOW + "2. Tuple:" + Style.RESET_ALL)
print(Fore.GREEN + " -Mirip dengan list, tetapi tidak dapat diubah setelah dibuat.\n", "-Dibuat menggunakan tanda kurung biasa ( ).\n", "-Memungkinkan duplikasi item.\n", "-Umumnya lebih cepat daripada list untuk operasi baca.\n", "-Contoh: my_tuple = (1, 2, 3, 'a', 'b', 'c').\n", "-Akses elemen menggunakan indeks: my_tuple[0].\n" + Style.RESET_ALL)

# Set
print(Style.BRIGHT + Fore.YELLOW + "3. Set:" + Style.RESET_ALL)
print(Fore.GREEN + " -Koleksi item yang tidak berurutan dan tidak terindeks.\n", "-Dapat diubah setelah dibuat, tetapi elemen-elemennya harus tidak dapat diubah setelah dibuat.\n", "-Tidak memungkinkan duplikasi item.\n", "-Dibuat menggunakan kurung kurawal { } atau fungsi set().\n", "-Berguna untuk banyak operasi matematika.\n", "-Contoh: my_set = {1, 2, 3, 'a', 'b', 'c'}.\n", "-Tidak bisa mengakses elemen dengan indeks.\n" + Style.RESET_ALL)

# Dictionary
print(Style.BRIGHT + Fore.YELLOW + "4. Dictionary:" + Style.RESET_ALL)
print(Fore.GREEN + " -Koleksi pasangan key-value yang tidak berurutan.\n", "-Dapat diubah setelah dibuat.\n", "-Key harus unik dan tidak dapat diubah setelah dibuat(biasanya string atau angka).\n", "-Dibuat menggunakan kurung kurawal { } dengan format key:value.\n", "-Sangat efisien untuk pencarian, penyisipan, dan penghapusan.\n", "-Contoh: my_dict = {'nama': 'Aldiyan', 'age': 19, 'Kota': 'Temanggung'}.\n", "-Akses nilai menggunakan key: my_dict['nama'].\n" + Style.RESET_ALL)

# Weekly Exercise 2
print("\nWeekly Exercise 2:")
dataDiri = {
    "Nama"          : "Aldiyan Setyo Nugroho",
    "Kelas"         : "01",
    "Tanggal Lahir" : "12 Oktober 2005",
    "No HP"         : "081234567890",
    "Alamat"        : "Jl.Raya No. 123",
    "Hobi"          : ["Membaca", "Bermain Gitar", "Olahraga"]
}

# Fungsi untuk mencetak data dengan warna
def cetak_data(key, value):
    print(f"{Fore.YELLOW}{key}{Style.RESET_ALL}: {Fore.CYAN}{value}{Style.RESET_ALL}")

# Menampilkan data diri
print(f"{Back.BLUE}{Fore.WHITE} Data diri {Style.RESET_ALL}")

for key, value in dataDiri.items():
    if key == "Hobi":
        print(f"{Fore.YELLOW}Hobi:{Style.RESET_ALL}")
        for index, hobi in enumerate(value, 1):
            print(f"  {Fore.GREEN}{index}. {hobi}{Style.RESET_ALL}")
    else:
        cetak_data(key, value)