# Kishan Suhi
# CCC - '10 J2: Up and Down

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nikky_steps = 0
byron_steps = 0

nikky_cycle = a + b
nikky_full_cycles = s // nikky_cycle
nikky_remaining_steps = s % nikky_cycle

nikky_steps = nikky_full_cycles * (a - b)
if nikky_remaining_steps <= a:
    nikky_steps += nikky_remaining_steps
else:
    nikky_steps += a - (nikky_remaining_steps - a)

byron_cycle = c + d
byron_full_cycles = s // byron_cycle
byron_remaining_steps = s % byron_cycle

byron_steps = byron_full_cycles * (c - d)
if byron_remaining_steps <= c:
    byron_steps += byron_remaining_steps
else:
    byron_steps += c - (byron_remaining_steps - c)

if nikky_steps > byron_steps:
    print("Nikky")
elif byron_steps > nikky_steps:
    print("Byron")
else:
    print("Tied")