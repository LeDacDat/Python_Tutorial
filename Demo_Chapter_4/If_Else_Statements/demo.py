import math

x = float(input("Nhap vao diem trung binh:"))

if x >=8.5 and x<=10:
    print("Xuat sac")
elif x>=8 and x<8.5:
    print("Gioi")
elif x>=6.5 and x<8:
    print("Kha")
elif x>=5 and x<6.5:
    print("Trung binh")
elif x>=0 and x<5:
    print("Yeu")
else:
    print("Diem nhap vao khong hop le!")
