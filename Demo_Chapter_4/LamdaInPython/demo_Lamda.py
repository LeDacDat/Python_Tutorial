#Example


kiemTraSoChan = lambda a : (a%2==0)

print(kiemTraSoChan(5))
print(kiemTraSoChan(4))

tinhTong = lambda a,b : (a+b)
print(tinhTong(5,10))

def hamMu(n):
    return lambda x : x**n

hamMu2 = hamMu(2)
hamMu3 = hamMu(3)

print(hamMu2(3))
print(hamMu3(3))

#Example

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
