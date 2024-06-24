def max_burgers(A, B):
    return min(A, B)
T = int(input())
for _ in range(T):
    A, B = map(int, input().strip().split())
    print(max_burgers(A, B))
