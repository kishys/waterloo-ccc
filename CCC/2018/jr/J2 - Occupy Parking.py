# Kishan Suhi
# CCC - '18 J2: Occupy Parking

spaces = int(input())
counter = 0

lot1 = input()
lot2 = input()

for i in range(spaces):
    check1 = lot1[i]
    check2 = lot2[i]
    if check1 == "C" and check2 == "C":
      counter += 1

print(counter)