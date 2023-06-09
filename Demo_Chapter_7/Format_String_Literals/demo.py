import math

#Formatted String Literals

#Example 1
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.

#Example 2
name = 'Le Dac Dat'
age = 21
print(f'{name:10} ==> {age:10d}')
# Le Dac Dat ==>         21

#Example 3
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

#Example 4
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
#My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
#My hovercraft is full of 'eels'.