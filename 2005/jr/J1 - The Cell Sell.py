# Kishan Suhi
# CCC - '05 J1: The Cell Sell

daytime_minutes = int(input(""))
evening_minutes = int(input(""))
weekend_minutes = int(input(""))

if daytime_minutes > 100:
    daytime_cost_A = (daytime_minutes - 100) * 0.25
else:
    daytime_cost_A = 0
evening_cost_A = evening_minutes * 0.15
weekend_cost_A = weekend_minutes * 0.20
total_cost_A = daytime_cost_A + evening_cost_A + weekend_cost_A

if daytime_minutes > 250:
    daytime_cost_B = (daytime_minutes - 250) * 0.45
else:
    daytime_cost_B = 0
evening_cost_B = evening_minutes * 0.35
weekend_cost_B = weekend_minutes * 0.25
total_cost_B = daytime_cost_B + evening_cost_B + weekend_cost_B

print(f"Plan A costs {total_cost_A:.2f}")
print(f"Plan B costs {total_cost_B:.2f}")

if total_cost_A < total_cost_B:
    print("Plan A is cheapest.")
elif total_cost_B < total_cost_A:
    print("Plan B is cheapest.")
elif total_cost_A == total_cost_B:
    print("Plan A and B are the same price.")