# Contoh 1
for i in range (2) :      # Perulangan tingkat pertama
    print("Perulangan luar : ", i)
    for j in range (10) :  # Perulangan tingkat kedua
        print("Perulangan dalam : ", j)
        if j == 1:
            break         # Menghentikan perulangan jika j = 1

"""
Output :
Perulangan luar :  0
Perulangan dalam :  0
Perulangan dalam :  1
Perulangan luar :  1
Perulangan dalam :  0
Perulangan dalam :  1

"""

# Contoh 2
for huruf in 'Maz deus' :
    if huruf == ' ' :
        break
    print('Huruf saat ini : {}'.format(huruf))

"""
Output :

"""