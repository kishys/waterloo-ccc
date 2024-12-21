# Kishan Suhi
# CCC - '21 J2: Silent Auction

ppl = []
price = []

people = int(input())
for i in range(people):
    askppl = input()
    ppl.append(askppl)
    askprice = int(input())
    price.append(askprice)

highest = price[0]
top = ppl[0]

for i in range(people):
    if price[i] > highest:
        highest = price[i]
        top = ppl[i]

print(top)