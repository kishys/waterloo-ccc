# Kishan Suhi
# CCC - '09 J2: Old Fishin' Hole

trout_points = int(input(""))
pike_points = int(input(""))
pickerel_points = int(input(""))
total_points_allowed = int(input(""))

count = 0


for bt in range(total_points_allowed // trout_points + 1):
    for np in range(total_points_allowed // pike_points + 1):
        for yp in range(total_points_allowed // pickerel_points + 1):
            if bt * trout_points + np * pike_points + yp * pickerel_points <= total_points_allowed and (bt > 0 or np > 0 or yp > 0):
                print(f"{bt} Brown Trout, {np} Northern Pike, {yp} Yellow Pickerel")
                count += 1

print(f"Number of ways to catch fish: {count}")