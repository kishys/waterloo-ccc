# Kishan Suhi
# CCC - '06 J1: Canadian Calorie Counting

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

burger_calories = [0, 461, 431, 420, 0]
side_calories = [0, 100, 57, 70, 0]
drink_calories = [0, 130, 160, 118, 0]
dessert_calories = [0, 167, 266, 75, 0]


total_calories = burger_calories[burger] + side_calories[side] + drink_calories[drink] + dessert_calories[dessert]


print(f"Your total Calorie count is {total_calories}.")