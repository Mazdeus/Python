# Ternary operators
lulus = True
print("Selamat kamu lulus") if lulus else print("Mohon maaf kamu tidak lulus")

"""
Output :
Selamat kamu lulus

"""

# Versi biasa 
lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")

"""
Output:
selamat
"""

# Ternary Tuples
lulus2 = True
kelulusan = ("Mohon maaf anda tidak lulus","Selamat, kamu lulus")[lulus2]
print(kelulusan)

"""
Output:
Selamat, kamu lulus
"""