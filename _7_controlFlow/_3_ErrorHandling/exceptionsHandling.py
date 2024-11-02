# Contoh exceptions
# z = 0
# print(1/z)

# """
# Output :
# Traceback (most recent call last):
#   File "d:\DICODING\Machine-Learning\Memulai-Pemrograman-Python\Python\7-controlFlow\3-ErrorHandling\exceptionsHandling.py", line 3, in <module>
#     print(1/z)
#           ~^~
# ZeroDivisionError: division by zero

# """

# Terapkan try-except
# z = 0
# try :
#     print(1/z)
# except ZeroDivisionError :
#     print("Anda tidak bisa membagi angka dengan nol")

# """
# Output :
# Anda tidak bisa membagi angka dengan nol

# """


# Contoh lengkap try-except
var_dict = {"rata-rata" : "1.0"}
try :
    print(f"rata-rata adalah {var_dict['rata-rata']}")
except KeyError :
    print("Key tidak ditemukan!")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")


"""
Output :
rata-rata adalah 1.0
Kode ini dieksekusi jika tidak ada exception.
Kode ini dieksekusi terlepas dari ada atau tidaknya exception.

"""