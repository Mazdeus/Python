#----------------------------
# x = (1, "Dicoding", 1+3j)
# print(type(x))

# """
# Output:
# <class 'tuple'>
# """
#----------------------------

#----------------------------
# x = (5, 'program', 1+3j)
# print(x[1])
# print(x[0:3])

# """ 
# Output:
# program
# (5, 'program', (1+3j))
# """
#-------------------------------

x = (5, 'program', 1+3j)
x[1] = 'Dicoding'

"""
Output:
'tuple' object does not support item assignment
"""