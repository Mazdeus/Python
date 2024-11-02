import pandas as pd

# Membuat dataframe dari dictionary
data = {
    'Nama' : ['John','Deus','Jami','Roy'],
    'Usia' : [20,15,30,50],
    'Pekerjaan' : ['Engineer','Teacher','Designer','Doctor']
}

df = pd.DataFrame(data)

# Menampilkan DataFrame
print(df)


"""
Output :
   Nama  Usia Pekerjaan
0  John    20  Engineer
1  Deus    15   Teacher
2  Jami    30  Designer
3   Roy    50    Doctor

"""