# Kishan Suhi
# CCC - '10 J1: What is n, daddy?

thenumber = int(input())

"""
All Posibilities

10 	- (5,5)
9 	- (5,4)
8	- (4,4),(5,3)
7	- (5,2),(4,3)
6	- (5,1),(4,2),(3,3)
5	- (5,0),(4,1),(3,2)
4 	- (4,0),(3,1),(2,2)
3	- (3,0),(2,1)
2	- (2,0),(1,1)
1	- (1,0)
"""

if thenumber == 10 or thenumber == 9 or thenumber == 1:
    print(1)
elif thenumber == 2 or thenumber == 3 or thenumber == 7 or thenumber == 8:
    print(2)
else:
    print(3)