x = True
print(type(x))

x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""

# Boolean Conversation
"""
We've seen int(), which turns things into ints, and float(), which turns things into floats, so you might not be surprised to hear that Python has a bool() function which turns things into bools.

"""

print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"

"""
We can use non-boolean objects in if conditions and other places where a boolean would be expected. Python will implicitly treat them as their corresponding boolean value:
"""

if 0:
    print(0)
elif "spam":
    print("spam")