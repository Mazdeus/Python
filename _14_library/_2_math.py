import math

print("It's math! It has type {}".format(type(math)))

print(dir(math))

#============================================================

"""Jika kita tahu bahwa kita akan sering menggunakan fungsi matematika, kita dapat 
mengimpornya dengan nama alias yang lebih pendek untuk menghemat pengetikan 
(meskipun dalam kasus ini “matematika” sudah cukup singkat).

"""
import math as mt
mt.pi

# Kita bisa merujuk ke semua variable yang ada di library math 
from math import *
"""
import * membuat semua variabel modul dapat diakses secara 
langsung oleh Anda (tanpa awalan titik-titik).
"""

print(math.sqrt(49))
print(math.pi)

"""
Output :
7.0
3.141592653589793
"""