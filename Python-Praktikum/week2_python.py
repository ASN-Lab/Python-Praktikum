
# Tipe Data di Python

# Merubah Nilai Data

# Mengubah Nilai Data ke Tipe yang Berbeda

# Mengubah integer menjadi string
x = 10  # x adalah integer
x = str(x)  # Sekarang x adalah string "10"

# Mengubah string menjadi float
angka = "3.14"  # angka adalah string
angka = float(angka)  # Sekarang angka adalah float 3.14

# Mengubah float menjadi integer
y = 7.9  # y adalah float
y = int(y)  # Sekarang y adalah integer 7 (bagian desimal dibuang)

# Error Dalam Pengubahan Nilai Data ke Tipe Data yang Berbeda

# Perubahan nilai yang tidak valid:

# mengubah tipe data string ke integer
# x = "hello"
# y = int(x)

print(x)

# Perubahan nilai yang tidak sesuai dengan konteks:

# mengubah nilai dari tipe data float, menjadi integer
x = 3.14
y = int(x)  # menghapus nilai yang semula desimal menjadi bilangan bulat
print(y)

# Perubahan nilai yang tidak diizinkan:

# perubahan yang tidak diizinkan
x = (1, 2, 3)
y = list(x)  # untuk line ini masih diizinkan
# z = x.append(4)  # line ini akan menyebabkan error

# Merubah Tipe Data

# String -> Integer

# merubah string ke integer
angka_str = "25"
angka_int = int(angka_str)  # Sekarang variabel angka_int adalah integer 25

# Integer->String

# mengubah integer ke string
usia = 20
usia_str = str(usia)  # Sekarang variabel usia_str adalah string "20"

# Integer->Float

# merubah integer ke float
nilai = 10
nilai_float = float(nilai)  # Sekarang variabel nilai_float adalah float 10.0

# Boolean

# Untuk mempresentasikan nilai Booleaan menggunakan true dan false.

#     True: Merepresentasikan kondisi yang benar.

#     False: Merepresentasikan kondisi yang salah.

# Operasi perbandingan digunakan untuk membandingkan dua nilai atau variabel. Hasil dari operasi ini adalah nilai Boolean (True atau False).

# Operasi perbandingan
x = 10
y = 5

print(x > y)   # True (karena 10 lebih besar dari 5)
print(x == y)  # False (karena 10 tidak sama dengan 5)
print(x < y)   # False (karena 10 tidak lebih kecil dari 5)

# Python menyediakan operasi logika seperti and, or, dan not untuk menggabungkan atau memodifikasi nilai Boolean.

#     and: Mengembalikan True jika kedua operand bernilai True.
#     or: Mengembalikan True jika salah satu operand bernilai True.
#     not: Mengembalikan negasi dari nilai Boolean (mengubah True menjadi False dan sebaliknya).

# Operasi logika
a = True
b = False

print(a and b)
print(a or b)
print(not a)

# Boolean dalam Kondisi (Conditional Statements)

nilai = 85

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")

# Konversi ke Boolean

    # Angka 0 (baik integer maupun float)
    # String kosong ""
    # List kosong []
    # Tuple kosong ()
    # Set kosong set()
    # Dictionary kosong {}

# Sedangkan semua nilai lainnya dianggap True.
# Latihan Pemrograman

# 1. Latihan Pertama

# kodingan yang sudah diperbaiki
panjang = 20.5
tinggi = 10
lebar = 25

keliling = 2 * (panjang + lebar)
luas = panjang * lebar
volume = panjang * lebar * tinggi

print("Panjang = " + str(panjang))
print("Lebar = " + str(lebar))
print("Tinggi = " + str(tinggi))
print("Keliling = " + str(keliling))
print("Volume = " + str(volume))

# 2. Latihan Kedua

# Data nilai mahasiswa
data_mahasiswa = {
    'Shafira': {'Kalkulus 1': 85, 'Metode Statistika': 75},
    'Amanda': {'Kalkulus 1': 80, 'Metode Statistika': 90},
    'Aditya': {'Kalkulus 1': 75, 'Metode Statistika': 80},
    'Nedia': {'Kalkulus 1': 95, 'Metode Statistika': 80},
    'Widya': {'Kalkulus 1': 85, 'Metode Statistika': 85},
    'Hanif': {'Kalkulus 1': 75, 'Metode Statistika': 90},
    'Andi': {'Kalkulus 1': 70, 'Metode Statistika': 75},
    'Dhanar': {'Kalkulus 1': 85, 'Metode Statistika': 85},
    'Hikma': {'Kalkulus 1': 80, 'Metode Statistika': 75},
}

# 1. Rata-rata nilai Shafira pada kedua mata kuli
rata_shafira = (data_mahasiswa['Shafira']['Kalkulus 1'] + data_mahasiswa['Shafira']['Metode Statistika']) / 2
print(f"Rata-rata nilai Shafira: {rata_shafira}")

# 2. Jumlah nilai Hanif dan Andi untuk setiap mata kuliah
jumlah_hanif_andi = (data_mahasiswa['Hanif']['Kalkulus 1'] + data_mahasiswa['Hanif']['Metode Statistika'] +
                     data_mahasiswa['Andi']['Kalkulus 1'] + data_mahasiswa['Andi']['Metode Statistika'])
print(f"Jumlah nilai Hanif dan Andi: {jumlah_hanif_andi}")

# 3. Rata-rata nilai Widya, Dhanar, Hikma, dan Nedia pada masing-masing mata kuliah
rata_kalkulus_4_mahasiswa = (data_mahasiswa['Widya']['Kalkulus 1'] + data_mahasiswa['Dhanar']['Kalkulus 1'] +
                             data_mahasiswa['Hikma']['Kalkulus 1'] + data_mahasiswa['Nedia']['Kalkulus 1']) / 4
rata_metode_4_mahasiswa = (data_mahasiswa['Widya']['Metode Statistika'] + data_mahasiswa['Dhanar']['Metode Statistika'] +
                           data_mahasiswa['Hikma']['Metode Statistika'] + data_mahasiswa['Nedia']['Metode Statistika']) / 4
print(f"Rata-rata nilai Kalkulus 1 untuk Widya, Dhanar, Hikma, dan Nedia: {rata_kalkulus_4_mahasiswa}")
print(f"Rata-rata nilai Metode Statistika untuk Widya, Dhanar, Hikma, dan Nedia: {rata_metode_4_mahasiswa}")

# 4. Rata-rata nilai mata kuliah Kalkulus 1 untuk setiap mahasiswa
rata_kalkulus_setiap = sum([data_mahasiswa[mahasiswa]['Kalkulus 1'] for mahasiswa in data_mahasiswa]) / len(data_mahasiswa)
print(f"Rata-rata nilai Kalkulus 1 untuk setiap mahasiswa: {rata_kalkulus_setiap}")

# 5. Rata-rata nilai mata kuliah Metode Statistika untuk setiap mahasiswa
rata_metode_setiap = sum([data_mahasiswa[mahasiswa]['Metode Statistika'] for mahasiswa in data_mahasiswa]) / len(data_mahasiswa)
print(f"Rata-rata nilai Metode Statistika untuk setiap mahasiswa: {rata_metode_setiap}")

# 3. Latihan Ketiga

# Data karyawan
gaji_pokok = 5000000 
hari_kerja = 22       
potongan_per_hari = gaji_pokok / hari_kerja  

# 1. Gaji pada bulan Agustus jika Dwi tidak masuk kerja selama 3 hari
hari_tidak_masuk = 3
potongan_gaji = potongan_per_hari * hari_tidak_masuk
gaji_agustus = gaji_pokok - potongan_gaji
print(f"Gaji Dwi pada bulan Agustus (setelah potongan 3 hari): Rp {gaji_agustus:,.0f}")

# 2. Tunjangan bagi karyawan yang bekerja lebih dari 5 tahun sebesar 10% dari total gaji
masa_kerja = 6 
tunjangan = 0
if masa_kerja > 5:
    tunjangan = 0.1 * gaji_agustus
print(f"Tunjangan untuk Dwi (masa kerja > 5 tahun): Rp {tunjangan:,.0f}")

# 3. Gaji total pada bulan Agustus jika Dwi mendapatkan tugas lembur selama 5 jam
upah_lembur_per_jam = 10000
jumlah_jam_lembur = 5
upah_lembur = upah_lembur_per_jam * jumlah_jam_lembur
gaji_total = gaji_agustus + tunjangan + upah_lembur
print(f"Gaji total Dwi pada bulan Agustus (termasuk lembur): Rp {gaji_total:,.0f}")