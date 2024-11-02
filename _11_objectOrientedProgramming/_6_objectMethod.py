class Mobil :
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self) :
        self.kecepatan += 20

mobil_1 = Mobil("Biru", "Daihatsu", 170)
print("Sebelum ditambahkan : ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()

print("Setelah ditambahkan")
print(mobil_1.kecepatan)

"""
Output :
Sebelum ditambahkan : 
170
Setelah ditambahkan
190

"""

# Contoh : kita tidak bisa memanggil method diatas langsung dari classnya
# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
    
#     def tambah_kecepatan(self):
#         self.kecepatan += 10
        
# Mobil.tambah_kecepatan()

# """
# Output:
# Traceback (most recent call last):
#   File "/home/glot/main.py", line 10, in <module>
#     Mobil.tambah_kecepatan()
# TypeError: tambah_kecepatan() missing 1 required positional argument: 'self'
# """