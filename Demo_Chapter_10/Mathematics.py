#math

import math

pi = math.pi
print(pi)
print(math.cos(pi/4))

a = math.log(1024,2)
print(a)
#10
b = math.sqrt(25)
print(b)
#5
c = math.pow(2,4)
print(c)
#16
#.................
#random

import random

#seed ham nay cho bo so gia ngau nhien
random.seed(5)
print(random.random())

#randint
x = random.randint(1,10) #random.randint lay ra so nguyen bat ki trong khoang tu 1-10
print(x)
#randrange
c = random.randrange(2,10,2)
print(c)

#choice ham nay cho phep chon mot phan tu ngau nhien
cards = ['ace_spades','10_hearts','3_diamonds','king_hearts']
a = random.choice(cards)
print(a)
#shuffle ham nay xao tron danh sach cac phan tu
cards = ['ace_spades','10_hearts','3_diamonds','king_hearts']
random.shuffle(cards)
print(cards)


#statistics
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
#tinh trung binh trong data
tb = statistics.mean(data)
print(tb)
#Tinh trung vi trong data
tv = statistics.median(data)
print(tv)
#Tinh phuong sai
ps = statistics.variance(data)
print(ps)
