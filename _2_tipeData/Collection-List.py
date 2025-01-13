# x = [1, 2.2, 'Dicoding']
# print(type(x))

# """
# Output: 
# <class ‘list’>
# """

#-----------------------------------

# x = [1, 'Dicoding', True, 1.0]

# print(x[2])

# """ 
# Output:
# True
# """

#------------------------------------
# x = [1, 2.2, 'Dicoding']
# x[0] = 'Indonesia'
# print(x)

# """
# Output:
# ['Indonesia', 2.2, 'Dicoding']
# """

#------------------------------------
# x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

# print(x[0])
# print(x[2])
# print(x[-1])
# print(x[-3])


# """
# Output:
# laptop
# mouse
# microphone
# keyboard
# """

#---------------------------------
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""

# List Comprehensiions
squares = [n**2 for n in range(10)]
squares

"""
Output:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

"""
Tanpa list comprehensions:
squares = []
for n in range(10):
    squares.append(n**2)
squares
"""

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Contoh pakai if
short_planets = [planet for planet in planets if len(planet) < 6]
short_planets

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets

# Tanpa list comprehensions
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

# Pakai list comprehensions
def count_negatives(nums):
    return len([num for num in nums if num < 0])

def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])