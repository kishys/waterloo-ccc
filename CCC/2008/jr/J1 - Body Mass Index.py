# Kishan Suhi
# CCC - '08 J1: Body Mass Index?


weight = float(input())
height = float(input())

doubleheight = height**2

bmi = weight / doubleheight

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 25:
    print("Normal weight")
elif bmi > 25:
    print("Overweight")