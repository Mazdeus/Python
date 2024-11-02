# Versi 1
# angka = [1,2,3,4,5]
# pangkat = []
# for n in angka :
#     pangkat.append(n**2)
# print(pangkat)

# """
# Output :
# [1, 4, 9, 16, 25]
# """

# Versi 2
# angka = [1,2,3,4,5]
# pangkat = [n**2 for n in angka]
# print(pangkat)

# """
# Output :
# [1, 4, 9, 16, 25]
# """

# latihan isi var evenNumber dengan range dari 0 hingga 500 yang termasuk genap, termasuk 0 dan 500
evenNumber = []
for i in range (0,501,2) :
    evenNumber.append(i)
print(evenNumber)
