# Contoh 

# Luas pertama
panjang = 5
lebar = 11

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 20

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

"""
Output:
55
80
"""


# Bandingkan dengan menerapkan subprogram yaitu fungsi

def mencari_luas_persegi_panjang(panjang,lebar) :
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,11)
print(persegi_panjang_pertama)

persegi_panjang_pertama = mencari_luas_persegi_panjang(4,20)
print(persegi_panjang_pertama)

"""
Output:
55
80
"""

# Adding optional argument with default to the functions turns out to be easy 
def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")