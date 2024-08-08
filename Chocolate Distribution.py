import math
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    min_children = math.ceil(N / 2)
    max_children = N
    print(min_children, max_children)
