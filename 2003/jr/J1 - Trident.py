# Kishan Suhi
# CCC - '03 J1: Trident

column = int(input(""))
space = int(input(""))
handle = int(input(""))

# Column & Space 
for i in range(column):
    print("*" + (" " * space) + "*" + (" " * space) + "*")

# Middle Beam
print("*" + "*" * space + "*" + "*" * space + "*")

# Handle
handle_width = (3 + 2 * space) // 2  
for i in range(handle):
    print(" " * handle_width + "*")