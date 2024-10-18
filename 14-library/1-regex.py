"""
Pada variabel pattern di bawah, ^a berarti kita ingin 
mencari teks dengan awalan 'a', dan s$ berarti kita 
ingin mencari string berakhiran 's'.

"""

import re     # Import modul regex
pola = '^a...s$'
string_tes = 'abyss'
hasil = re.match(pola, string_tes)

if hasil:
    print("Pencarian berhasil")
else:
    print("Pencarian gagal")

"""
Output :
Pencarian berhasil
"""