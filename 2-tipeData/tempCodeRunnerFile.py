# x = {1,2,7,2,3,13,3}
# print(x[0])

# """
# Output:
# 'set' object is not subscriptable
# """

#------------------------------------

# x = {1, 2, 7, 2, 3, 13, 3}
# print(x)
# print(type(x))

# """
# Output:
# {1, 2, 3, 7, 13}
# <class 'set'>
# """

#-------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

