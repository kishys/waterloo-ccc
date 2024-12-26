# Kishan Suhi
# CCC - '13 J2: Rotating Letters

word = input("").upper()
ltrs = ["I", "O", "S", "H", "Z", "X", "N"]

a = True
for i in word:
    if i not in ltrs:
        a = False
        break

if a:
    print("YES")
else:
    print("NO")