# Exercise 1

# soal 1
# membuat file dengan ekstensi .txt

# soal 2
# buka file .txt yang sudah dibuat
with open("week3_data.txt", "r") as file:
    biodata = file.readlines()

# Extract informasi dari txt
nama = biodata[0].split(": ")[1].strip()
program_studi = biodata[1].split(": ")[1].strip()
email = biodata[5].split(": ")[1].strip()

# Tampilkan informasi sesuai data
print("Nama:", nama)
print("Program Studi:", program_studi)
print("Email:", email)

# soal 3
# Buka file txt tadi
with open("week3_data.txt", "r") as file:
    # Membaca isi file
    biodata = file.readlines()

# Mengumpulkan data dari file
nama = biodata[0].split(": ")[1].strip()
npm = biodata[2].split(": ")[1].strip()
program_studi = biodata[1].split(": ")[1].strip()
alamat = biodata[3].split(": ")[1].strip()

# buat file .txt baru untuk menyimpan 
with open("data_ekstrak_week3.txt", "w") as new_file:
    new_file.write("Nama: " + nama + "\n")
    new_file.write("NPM: " + npm + "\n")
    new_file.write("Program Studi: " + program_studi + "\n")
    new_file.write("Alamat: " + alamat + "\n")

# Exercise 2
# memperbaiki kodingan agar bisa di run

print("Selamat datang di Toko Maju Jaya")
print("Senin, 4 September 2023       13.05")
print(" ")

print("DAFTAR BELANJA:")
item1 = "Sabun"
item2 = 'Shampo'
item3 = "Mie instant"
item4 = "Detergen"
harga1 = 10000
harga2 = 15000
harga3 = 5000
harga4 = 17500

total = harga1 + harga2 + harga3 + harga4

print(item1, "      = Rp ", harga1)
print(item2, "     = Rp ", harga2)
print(item3, "= Rp ", harga3)
print(item4, "   = Rp ", harga4)

print(" ")
print("Total = Rp ", total)

with open('Kuitansi.txt', 'w') as writefile:
    writefile.write("Selamat Datang di Toko Maju Jaya\n")
    writefile.write(" \n")
    writefile.write("Kuitansi - 4 September 2023\n")
    writefile.write(" \n")
    writefile.write(item1 + " = Rp " + str(harga1) + "\n")
    writefile.write(item2 + " = Rp " + str(harga2) + "\n")
    writefile.write(item3 + " = Rp " + str(harga3) + "\n")
    writefile.write(item4 + " = Rp " + str(harga4) + "\n")
    writefile.write(" \n")
    writefile.write("Total Belanja = Rp " + str(total))


