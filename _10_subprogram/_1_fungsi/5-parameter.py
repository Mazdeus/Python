# positional-or-keyword
def greeting(nama, pesan) :
    return "Halo, " + nama + "! " + pesan

print(greeting("Mazdeus", "Selamat pagi!"))
print(greeting(pesan = "Selamat pagi!", nama = "Mazdeus"))

"""
Output :
Halo, Mazdeus! Selamat pagi!
Halo, Mazdeus! Selamat pagi!

"""

# Positional-Only
def penjumlahan(a,b,/) :
    return a + b

print(penjumlahan(10,20))

# print(penjumlahan(a=3, b=5)) # TypeError: penjumlahan() got some positional-only arguments passed as keyword arguments: 'a, b'

"""
Output :
30

"""

# keyword-only
def greeting(*, nama, pesan) :
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan = "Selamat malam!", nama = "Julius"))

# print(greeting("Selamat sore!","Dicoding"))       # TypeError: greeting() takes 0 positional arguments but 2 were given

"""
Output :
Halo, Julius! Selamat malam!

"""


# Var-Positional (Variadic Positional Parameter)

def hitung_total(*args) :
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1,2,3))

"""
Output :
<class 'tuple'>
6

"""


# Var-Keyword (Variadic Keyword Parameter)
def cetak_info(**kwargs) :
    info = ""
    for key, value in kwargs.items() :
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama = "Gampad", usia = "17", pekerjaan = "Python programmer"))

"""
Output :


"""