import colorama
from colorama import Fore, Style, init
init()

print(Style.BRIGHT + "\nWeek 9\n")
# 1. LIST
print("LIST")
# List: Terurut, bisa diubah, memperbolehkan duplikat
buah_list = ["apel", "pisang", "ceri", "apel"]  # List dengan duplikat
angka_list = [1, 2, 3, 4, 5]  # List dengan angka
campuran_list = ["halo", 42, True, 3.14]  # List dengan berbagai tipe data

print(f"List awal: {buah_list}")
print(f"Panjang list: {len(buah_list)}")
print(f"Item pertama: {buah_list[0]}")  # Mengakses dengan indeks
print(f"Item terakhir: {buah_list[-1]}")  # Indeks negatif
print(f"Potongan list: {buah_list[1:3]}")  # Pemotongan

# Mengubah list
buah_list[1] = "jeruk"  # Mengubah item
buah_list.append("anggur")  # Menambah item di akhir
buah_list.insert(1, "mangga")  # Menyisipkan pada posisi tertentu
print(f"List setelah diubah: {buah_list}")

# 2. TUPLE
print("\nTUPLE")
# Tuple: Terurut, tidak bisa diubah, memperbolehkan duplikat
buah_tuple = ("apel", "pisang", "ceri", "apel")
angka_tuple = (1, 2, 3, 4, 5)
tuple_tunggal = (1,)  # Tuple dengan satu item perlu koma

print(f"Tuple awal: {buah_tuple}")
print(f"Jumlah 'apel': {buah_tuple.count('apel')}")  # Menghitung kemunculan
print(f"Indeks 'pisang': {buah_tuple.index('pisang')}")  # Mencari indeks

# 3. SET (HIMPUNAN)
print("\nSET")
# Set: Tidak terurut, tidak bisa diubah, tidak ada duplikat
buah_set = {"apel", "pisang", "ceri", "apel"}  # Duplikat akan dihapus
print(f"Set awal: {buah_set}")

# Operasi set
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
print(f"Gabungan: {set1.union(set2)}")  # Menggabungkan set
print(f"Irisan: {set1.intersection(set2)}")  # Elemen yang sama
print(f"Selisih: {set1.difference(set2)}")  # Elemen di set1 tapi tidak di set2

# Menambah dan menghapus dari set
buah_set.add("jeruk")  # Tambah satu item
buah_set.update(["mangga", "anggur"])  # Tambah beberapa item
buah_set.remove("pisang")  # Hapus item
print(f"Set setelah diubah: {buah_set}")

# 4. DICTIONARY (KAMUS)
print("\nDICTIONARY")
# Dictionary: Terurut, bisa diubah, tidak ada duplikat kunci
mobil = {
    "merek": "Toyota",
    "model": "Avanza",
    "tahun": 2020,
    "warna": ["merah", "putih", "hitam"]
}

print(f"Dictionary awal: {mobil}")
print(f"Mengakses nilai: {mobil['merek']}")
print(f"Mengambil nilai dengan aman: {mobil.get('model')}")

# Mengubah dictionary
mobil["tahun"] = 2023  # Ubah nilai
mobil["harga"] = 250000000  # Tambah pasangan kunci-nilai baru
print(f"Dictionary setelah diubah: {mobil}")

# Metode dictionary
print(f"Kunci: {mobil.keys()}")
print(f"Nilai: {mobil.values()}")
print(f"Item: {mobil.items()}")

# WEEKLY EXERCISE
print("\nEXERCISE 1 ")
print("""
Perbedaan list, tuple, set, dan dictionary dalam Python:

1. LIST:
   - Menggunakan tanda []
   - Dapat diubah (mutable)
   - Terurut
   - Mengizinkan duplikat
   - Contoh: [1, 2, 3, 'a', 'b']

2. TUPLE:
   - Menggunakan tanda ()
   - Tidak dapat diubah (immutable)
   - Terurut
   - Mengizinkan duplikat
   - Contoh: (1, 2, 3, 'a', 'b')

3. SET:
   - Menggunakan tanda {}
   - Dapat diubah tetapi elemennya immutable
   - Tidak terurut
   - Tidak mengizinkan duplikat
   - Contoh: {1, 2, 3, 'a', 'b'}

4. DICTIONARY:
   - Menggunakan tanda {} dengan format key:value
   - Dapat diubah
   - Terurut (sejak Python 3.7)
   - Tidak mengizinkan duplikat pada key
   - Contoh: {'nama': 'Budi', 'umur': 25}
""")

# WEEKLY EXERCISE 2 
print("\nEXERCISE 2 ")

# Data mahasiswa menggunakan dictionary
data_mahasiswa = {
    "nama": "Aldiyan Setyo Nugroho",
    "kelas": "Rombel 2",
    "tanggal_lahir": "30 Februari 2005",
    "no_hp": "0812398623",
    "alamat": "Jl. Mawar No. 123, Magelang",
    "hobi": ["Membaca", "Berenang", "Main Gitar"]
}

for key, value in data_mahasiswa.items():
    if key == "hobi":
        print(f"{key.upper()}:")
        for index, hobi in enumerate(value, 1):
            print(f"{index}. {hobi}")
    else:
        print(f"{key.upper()}: {value}")

print(Style.RESET_ALL)