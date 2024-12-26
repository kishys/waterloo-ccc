# Kishan Suhi
# CCO - '96 P1: Train Swapping

def count_swaps(train):
    swaps = 0
    n = len(train)
    for i in range(n):
        for j in range(0, n - i - 1):
            if train[j] > train[j + 1]:
                train[j], train[j + 1] = train[j + 1], train[j]
                swaps += 1
    return swaps

test_cases = int(input(""))

for _ in range(test_cases):
    length = int(input(""))
    train = list(map(int, input("").split()))
    
    swap_count = count_swaps(train)
    print(f"Optimal train swapping takes {swap_count} swaps.")
