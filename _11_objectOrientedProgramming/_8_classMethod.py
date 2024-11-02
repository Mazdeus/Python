class Mobil :
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls) :
        print("Ini adalah method dari class Mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("Daihatsu")
mobil_1.intro_mobil()

"""
Output :
Ini adalah method dari class Mobil
Ini adalah method dari class Mobil

"""