
import math

#example 1
words = ['cat','window','iloveyou','metoo']
for x in words:
    print(x, len(x))

#example 2
users = {'hans':'actice','eleonore':'inactive','abc':'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
#example 3
# range in python

for i in range(5):
    print(i)

print(list(range(5,10)))
print((list(range(0,10,3))))

a = ['Mary', 'had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i])

#example
print(sum(range(4)))

# Tinh Tong

sum = 0
for i in range(10):
    sum += i;

print(sum)

