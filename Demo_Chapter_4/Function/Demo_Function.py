import math

def xinChao():
    print("Xin chao")

xinChao()
# Xin chao

def xinChao(hoVaTen):
    print("Xin chao :"+hoVaTen)

xinChao("Le Dac Dat")
#Xin chao : Le Dac Dat

def Sum(*var):
    sum = 0
    for i in var:
        sum+=i
    print(sum)

Sum(1,2,3,4)
# 10

def Tich(*value):
    tich = 1
    for i in value:
        tich*=i

    return tich

tich1 = Tich(2,3,4)
print(tich1)


#example

def fib(n):
    a, b = 0,1
    while a<n:
        print(a, end=' ')
        a,b = b, a+b
    print()

fib(100)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


