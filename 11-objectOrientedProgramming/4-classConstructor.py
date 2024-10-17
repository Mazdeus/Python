# Contoh 1
class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'

mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Biru"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)

"""
Output :
Merah
Merah
Biru
Merah

"""

# Contoh 2
class Mobil :
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil_1 = Mobil('Merah','Daihatsu',160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

"""
Output :
Merah
Daihatsu
160

"""