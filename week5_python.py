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

# Contoh nseted If (Number Checker)

num = 10

if num > 0:
    print ("Angka ini positif")
else:
    if num < 0:
        print ("Angka ini negative")
    else:
        print ("Angka ini adalah 0")