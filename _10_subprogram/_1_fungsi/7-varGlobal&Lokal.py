# variabel global

a = 10 # -----> variabel global

def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

"""
Output:
30
"""

# variabel lokal
def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)

"""
Output:
25
"""