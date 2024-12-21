# Kishan Suhi
# CCC - '19 J1: Winning Score

a = int(input(""))
b = int(input(""))
c = int(input(""))

d = int(input(""))
e = int(input(""))
f = int(input(""))

apple = a*3 + b*2 + c*1
banana = d*3 + e*2 + f*1

if apple > banana:
    print("A")
elif banana > apple:
    print("B")
else:
    print("T")