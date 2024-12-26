# Kishan Suhi
# CCC - '14 J2: Vote Count

length = int(input(""))
votes = input()

acount = 0
bcount = 0

for i in votes:
    if i == "A":
        acount += 1
    elif i == "B":
        bcount += 1

if acount > bcount:
    print("A")
elif acount < bcount:
    print("B")
else:
    print("Tie")