# Kishan Suhi
# CCC - '12 J1: Speed fines are not fine!

limit = int(input())
carspeed = int(input())

if carspeed > limit:
    over = carspeed - limit
    if over >= 1 and over <= 20:
        print("You are speeding and your fine is $100.")
    elif over >= 21 and over <= 30:
        print("You are speeding and your fine is $270.")
    elif over >= 31:
        print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")