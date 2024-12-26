# Kishan Suhi
# CCC - '23 J2: Chilli Peppers

spice = 0

a = int(input())  
for i in range(a):
    pepper = input()
    if pepper == "Poblano":
        spice += 1500
    elif pepper == "Mirasol":
        spice += 6000
    elif pepper == "Serrano":
        spice += 15500
    elif pepper == "Cayenne":
        spice += 40000
    elif pepper == "Thai":
        spice += 75000
    elif pepper == "Habanero": 
        spice += 125000

print(spice)