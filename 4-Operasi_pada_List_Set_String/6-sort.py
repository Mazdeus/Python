# Contoh 1
# kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
# kendaraan.sort()

# print(kendaraan)

# """
# Output:
#  ['helikopter', 'mobil', 'motor', 'pesawat']
# """

# membalikkan urutan
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

"""
Output:
 ['pesawat', 'motor', 'mobil', 'helikopter']

"""

# tidak bisa mengurutkan angka dan huruf sekaligus
# urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
# urutan.sort()

# print(urutan)

# """
# Output:
# TypeError: '<' not supported between instances of 'int' and 'str'
# """

# Huruf kapital lebih dahulu
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
['Pesawat', 'helikopter', 'mobil', 'motor']
"""