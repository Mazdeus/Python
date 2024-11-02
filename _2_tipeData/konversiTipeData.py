# integer >> float

# print(float(5))

# """
# Output:
# 5.0
# """

#------------------

# Konversi Float ke Integer

# print(int(5.6))
# print(int(-5.6)) 

# """ 
# Output:
# 5
# -5
# """

#------------------------

# KOnversi dari-dan-ke-string

# print(int("25"))
# print(str(25))
# print(float("25"))
# print(str(25.6))

# """
# Output:
# 25
# 25
# 25.0
# 25.6
# """

# Ketika pengujian validitasnya gagal
# print(int("1p"))

# """
# Output:
# ValueError: invalid literal for int() with base 10: '1p
# """

#---------------------

# Konversi kumpulan data

# print(set([1,2,3]))
# print(tuple({5,6,7}))
# print(list('hello'))

# """
# Output:
# {1,2,3}
# (5,6,7)
# ['h','e','l','l','o']
# """

#--------------------------

# Konversi list >> dict

# print(dict([[1,2],[3,4]]))

# """
# Output:
# {1:2, 3:4}
# """

# Konversi tuple >> dict
# print(dict([(3,26),(4,44)]))

# """
# Output:
# {3:26, 4:44}
# """

#---------------------

# Konversi set >> tuple
print(dict([{3,26},{4,44}]))

"""
Output:
{26: 3, 4: 44}
"""

