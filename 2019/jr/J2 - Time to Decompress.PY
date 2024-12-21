# Kishan Suhi
# CCC - '19 J2: Time to Decompress

counter = int(input())
lst = []

for i in range(counter):
    a = input().split()
    length = int(a[0])
    thetype = a[1]
    new = thetype * length
    lst.append(new)

for i in range(counter):
    print(lst[i])