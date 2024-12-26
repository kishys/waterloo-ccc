# Kishan Suhi
# CCC - '17 J2: Shifty Sum

base = int(input())
shift = int(input())

final = 0

for i in range(shift + 1):
    final += base * (10 ** i)

print(final)