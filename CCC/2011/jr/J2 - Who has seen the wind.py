# Kishan Suhi
# CCC - '11 J2: Who Has Seen The Wind

h = int(input())
M = int(input())

def altitude(t, h):
    return -6 * t**4 + h * t**3 + 2 * t**2 + t

touched_ground = False

for t in range(1, M + 1):
    if altitude(t, h) <= 0:
        print(f"The balloon first touches ground at hour:\n{t}")
        touched_ground = True
        break

if not touched_ground:
    print("The balloon does not touch ground in the given time.")