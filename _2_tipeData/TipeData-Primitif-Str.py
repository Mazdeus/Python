multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""


x = 'Dicoding'
print(x[0])

""" 
Output:
D
"""

"""
x = 'Dicoding'
x[0] = 'F'
"""

""" 
Output:
TypeError: 'str' object does not support item assignment
"""

name = "Perseus Evans"
print("Hello, nama saya {name}")
 
"""
Output: 
Hello, nama saya Perseus Evans
"""

name = "Perseus Evans"
print("Nama saya %s" % (name))
 
"""
Output: 
Nama saya Perseus Evans
"""

# String with a backslash
print('Pluto\'s a planet!')

# Newline
hello = "hello\nworld"
print(hello)

# Triple quotes
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello

# Example lain
print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

# String are squences
# Indexing
planet = 'Pluto'
planet[0]

# Yes, we can even loop over them
[char+'! ' for char in planet]

# planet[0] = 'B'
# planet.append doesn't work either

# check string claim , it is started with string or not which is stored in planet
claim = 'pluto is a planet!'
claim.startswith(planet)

# .format
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
# 2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))