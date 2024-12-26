# Kishan Suhi
# CCC - '14 J3: Double Dice

rounds = int(input(""))

p1 = 100
p2 = 100

for i in range(rounds):
    a = input("").split()
    player1 = int(a[0])
    player2 = int(a[1])
    if player1 > player2:
        p2 -= player1
    elif player2 > player1:
        p1 -= player2

print(p1)
print(p2)
