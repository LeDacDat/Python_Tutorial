import math
a = float(input("Nhap vao he so a:"))
b= float(input("Nhap vao he so b:"))
c = float(input("Nhap vao he so c:"))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem!")
        else:
            print("Phuong trinh vo nghiem!")
    else:
        x0 =  -c/b;
        print("Phuong trinh la phuong trinh bac nhat co nghiem  x ={0}".format(x0))
else:
    delta = b**2- 4*a*c
    if delta<0:
        print("phuong trinh vo nghiem!")
    elif delta == 0:
        kq = -b/2*a
        print("phuong trinh co nghiem kep x1 = x2 = {0}".format(round(kq,2)))
    else :
        x1 = (-b + math.sqrt(delta))/ 2*a
        x2 = (-b- math.sqrt(delta))/2*a
        print("phuong trinh co 2 nghiem phan biet")
        print("x1 = {0}".format(round(x1,2)))
        print("x2 = {0}".format(round(x2,2)))
