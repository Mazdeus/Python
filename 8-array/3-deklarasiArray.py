# Cara 1
# Mendefinisikan Isi Array
var_array = [1,2,3,4,5,6,7,8,9]
print(var_array)

"""
Output :
[1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

# Cara 2
# Mendefinisikan Nilai default
var_array = [0 for i in range(10)]
print(var_array)

"""
Output :
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""

# Mengubah nilai default menjadi nilai baru
var_array = [0 for i in range(10)]

for i in range(10) :
    var_array[i] = i

print(var_array)