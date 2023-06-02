#Strings in Python
#Example 1

print('spam eggs')
print('doesn\'t')
print("doesn't")

print('first line.\n second line')
print(r'C:\some\name')
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(3*'un' + 'ium')
print('Py''thon')
"""
prefix = 'Py'
prefix 'thon'
print(prefix)
"""

"""
Strings can be indexed (subscripted), with the first character having index 0. 
There is no separate character type; a character is simply a string of size one:
"""

word = 'Python'
print(word[0])
print(word[5])

print(word[-1])
print(word[-2])

print(word[:2])
print(word[4:])
print(word[-2:])
print(word[2:5])
print(word[:2] + word[2:])

print(len(word))
