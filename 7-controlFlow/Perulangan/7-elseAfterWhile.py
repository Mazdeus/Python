# Contoh 
count = 0
while count < 3 :
    print("Dicoding Indonesia")
    count += 1
else :
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == false).")

"""
Output :
Dicoding Indonesia
Dicoding Indonesia
Dicoding Indonesia
Blok else dieksekusi karena kondisi pada while salah (3<3 == false).
"""

# Contoh else after while dengan break
n = 10
while n > 0 :
    n = n - 1
    if n == 7 :
        break
    print(n)
else :
    print("Loop selesai")

"""
Output :
9
8
"""