# Kondisi di Python

# Kondisi statement

# Kondisi equal
a = 10
a == 15 # false

# Tanda lebih besar
b = 11
b > 10 # true

b = 5
b > 10 # false

# Tanda tidak persamaan

c = 3
c != 1 # True

c = 3
c != 3 # false

# Penggunaan tanda persamaan dalam membandingkan tipe data string

"One_Direction" == "One_Direction" # True
"Avenged" == "Slipknot" # False

# Penggunaan tanda tidak persamaan dalam membandingkan tipe data string

"One_Direction" != "Avenged" # True
"Avenged" != "Avenged" # False

# Pembandingan char

# Single Char
'X' > 'D' # True

# Multiple char
'BA' > 'AB' # True

# Multiple sign
"ba" >= "ba" # True

# Percabangan

# Contoh kasus

# Konser dengan batas umur

#age = 19
age = 18

#expression yang bisa true atau false
if age > 18:
    print("Kamu boleh masuk" )
print("Maju")




# Exercise

# Latiham 1

umur = input('Masukkan umur:')

if int(umur) >= 17:
    print ('Anda dapat membuat SIM')
elif int(umur) == 17:
    print ('Anda dapat membuat SIM')
else:
    print ('Anda tidak dapat membuat SIM')

# Latihan 2 dan 3

nilai = input('Masukkan nilai:')

if int(nilai) >= 90:
    print ('Grade anda A')
elif int(nilai) >=80:
    print ('Grade anda B+')
elif int(nilai) >=70:
    print ('Grade anda B')
elif int(nilai) >=60:
    print ('Grade anda C+')
elif int(nilai) >=50:
    print ('Grade anda C')
elif int(nilai) >=40:
    print ('Grade anda D')
else:
    print ('Grade anda E')

nilai = input('Masukkan nilai:')

if float(nilai) >= 80:
    print ('Grade anda A')
elif float(nilai) >= 77.5:
    print ('Grade anda A-')
elif float(nilai) >= 75:
    print ('Grade anda A/B')
elif float(nilai) >= 72.5:
    print ('Grade anda B+')
elif float(nilai) >= 70:
    print ('Grade anda B')
elif float(nilai) >= 67.5:
    print ('Grade anda B-')
elif float(nilai) >= 65:
    print ('Grade anda B/C')
elif float(nilai) >= 62.5:
    print ('Grade anda C+')
elif float(nilai) >= 60:
    print ('Grade anda C')
elif float(nilai) >= 55:
    print ('Grade anda C-')
elif float(nilai) >= 50:
    print ('Grade anda C/D')
elif float(nilai) >= 45:
    print ('Grade anda D+')
elif float(nilai) >= 40:
    print ('Grade anda D')
else:
    print ('Grade anda E')