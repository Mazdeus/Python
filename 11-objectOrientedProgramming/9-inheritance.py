class Mobil :
    def __init__(self, warna, merek, kecepatan) :
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self) :
        self.kecepatan += 10

class MobilSport(Mobil) :
    def turbo(self) :
        self.kecepatan +=50

# class mobil dasar
mobil_1 = Mobil("Putih", "Daihatsu", 160)
print(mobil_1.kecepatan)

# class mobil sport
mobil_sport_1 = MobilSport("Hitam", "Asmodeus", 170)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo
print(mobil_sport_1.kecepatan)


"""
Output :
160
170
170

"""