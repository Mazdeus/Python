# Deklarasi sekaligus inisialisasi nilai matriks
matriks = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]
     
print(matriks)

"""
Output:
[[1, 0, 0, 0, 0],[0, 1, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 1, 0],[0, 0, 0, 0, 1]]
"""

# Deklarasi dengan nilai default
matriks = [[0 for j in range(4)] for i in range(3)]
print(matriks)

"""
Output :
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

"""