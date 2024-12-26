# Kishan Suhi
# CCC - '16 J2: Magic Squares

negative = True


row1 = input("").split()
row1num1 = int(row1[0])
row1num2 = int(row1[1])
row1num3 = int(row1[2])
row1num4 = int(row1[3])

row2 = input("").split()
row2num1 = int(row2[0])
row2num2 = int(row2[1])
row2num3 = int(row2[2])
row2num4 = int(row2[3])

row3 = input("").split()
row3num1 = int(row3[0])
row3num2 = int(row3[1])
row3num3 = int(row3[2])
row3num4 = int(row3[3])

row4 = input("").split()
row4num1 = int(row4[0])
row4num2 = int(row4[1])
row4num3 = int(row4[2])
row4num4 = int(row4[3])

main = row1num1 + row1num2 + row1num3 + row1num4

if row2num1 + row2num2 + row2num3 + row2num4 != main:
    negative = False
if row3num1 + row3num2 + row3num3 + row3num4 != main:
    negative = False
if row4num1 + row4num2 + row4num3 + row4num4 != main:
    negative = False

if row1num1 + row2num1 + row3num1 + row4num1 != main:
    negative = False
if row1num2 + row2num2 + row3num2 + row4num2 != main:
    negative = False
if row1num3 + row2num3 + row3num3 + row4num3 != main:
    negative = False
if row1num4 + row2num4 + row3num4 + row4num4 != main:
    negative = False

if negative == False:
    print("not magic")
else:
    print("magic")