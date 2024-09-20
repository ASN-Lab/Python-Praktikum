# Nested If

# if condition_1:
#     if condition_1_a:
#         ...
#     elif condition_1_b:
#         ...
#     else:
#         ...
# elif condition_2:
#     if condition_2_a:
#         ...
#     else:
#         ...
# elif condition_3:
#     if condition_3_a:
#         ...
# else:
#     ...

# Contoh Nested If (Number Checker)

print("Number Checker")

num = float(input("Masukkan angka: "))

if num > 0:
    print("Angka ini positif\n")
elif num < 0:
    print("Angka ini negative\n")
else:
    print("Angka ini adalah 0\n")

# Contoh Nested If (Penglasifikasi umur)

print("Klasifikasi umur")

umur = int(input("Masukkan umur: "))

if umur >= 60:
    print("Anda adalah Lansia\n")
elif umur >= 18:
    print("Anda adalah Dewasa\n")
else:
    print("Anda adalah Anak-anak\n")

# Quiz



# Exercise 1
print ("Exercise 1\n")

tahun = int(input("Masukkan tahun: "))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print(f"Tahun {tahun} adalah tahun kabisat.\n")
        else:
            print(f"Tahun {tahun} bukan tahun kabisat.\n")
    else:
        print(f"Tahun {tahun} adalah tahun kabisat.\n")
else:
    print(f"Tahun {tahun} bukan tahun kabisat.\n")

# Exercise 2
print ("Exercise 2\n")

print("Mencari  nilai terbesar dari 3 angka")

num1 = float(input("Masukkan angka pertama  : "))
num2 = float(input("Masukkan angka kedua    : "))
num3 = float(input("Masukkan  angka ketiga  : "))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"Angka pertama   : {num1}")
print(f"Angka kedua     : {num2}")
print(f"Angka ketiga    : {num3}\n")
print(f"Angka terbesar adalah: {largest}\n")

# Exercise 3
print ("Exercise 3\n")

print("Kalkulator Pembayaran Pusat Belanja")

customer_type = input("Apakah anda member? (ya/tidak): ")

total_purchase = float(input("Masukkan total jumlah pembelian: \n"))

discount_percentage = 0

if total_purchase > 100000:
    discount_percentage = 3
    if total_purchase > 200000:
        discount_percentage = 4

if customer_type.lower() == "ya":
    discount_percentage += 2

discount_amount = (discount_percentage / 100) * total_purchase

total_payment = total_purchase - discount_amount

print(f"Total Pembelian     : Rp {total_purchase:.2f}")
print(f"Presentase Diskon   : {discount_percentage}%")
print(f"Jumlah Diskon       : Rp {discount_amount:.2f}")
print(f"Total Pembayaran    : Rp {total_payment:.2f}")

# Exercise 4
print ("Exercise 4\n")

print("Buat user baru")

username =  input("username : ")
email =     input("email    : ")
password =  input("password : ")

if username == "":
    print("Error: Harap isi bagian username.\n")
elif "@" not in email:
    print("Error: Email harus terdapat simbol '@'.\n")
elif len(password) <= 8:
    print("Error: Password harus lebih dari 8 karakter.\n")
else:
    print("Pembuatan user baru berhasil!")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: (password disembunyikan)")