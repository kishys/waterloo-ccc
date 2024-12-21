# Kishan Suhi
# CCC - '20 J2: Epidemiology

goal = int(input())
infect = int(input())
rate = int(input())
increase = infect
day = 0

while infect <= goal:
    increase *= rate
    infect += increase
    day += 1
print(day)