# cook your dish here
T = int(input().strip())
for _ in range(T):
    X = int(input().strip())
    min_incorrect = float('inf')
    for C in range(101):
        I = 3 * C - X
        if I >= 0 and C + I <= 100:
            min_incorrect = min(min_incorrect, I)
    print(min_incorrect)
