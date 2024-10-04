# Soal 1
print ("Pendeteksi jumlah bilangan ganjil dan genap pada NPM\n")  # judul program

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
      bilangan_genap
      bilangan_genap += 1
    else:
      # Jika ganjil, tambahkan ke variabel ganjil bilangan_ganjil
      bilangan_ganjil += 1
  # Mengembalikan hasil hitungan bilangan ganjil dan genap
  return bilangan_ganjil, bilangan_genap

# Menginputkan data berupa NPM
npm = int(input ("Masukkan NPM anda: "))
# Memanggil fungsi untuk menghitung bilangan ganjil dan genap
ganjil, genap = jumlah_bilangan(npm)
# Cetak hasil
print (f"Jumlah bilangan ganjil adalah: {ganjil}")
print (f"Jumlah bilangan genap adalah: {genap}")

# Soal 2
print ("\nSegitiga Angka dan Jumlah Kelipatan Tiap Baris\n")  # judul program

# Menginputkan jumlah baris dari segitiga angka
segitiga_angka = int(input("Jumlah baris: "))

# Pengulangan setiap baris
for i in range(1, segitiga_angka + 1):
  # Pengulangan setiap kolom dalam baris
  for j in range(1, i + 1):
    # Cetak hasil perkalian baris dan kolom
    print(j * i, end=" ")
  # Pindah ke baris berikutnya setelah setiap baris
  print()