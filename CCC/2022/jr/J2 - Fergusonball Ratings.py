# Kishan Suhi
# CCC - '22 J2: Ferhusonball Ratings

ranks = []
teams = int(input())
for i in range(teams):
    score = int(input())
    foul = int(input())
    final = score * 5 - foul * 3
    ranks.append(final)

counter = 0
ranks.sort()

for i in ranks:
    if i > 40:
        counter += 1

if counter == len(ranks):
    print(f"{counter}+")
else:
    print(counter)