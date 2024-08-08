T = int(input().strip())
for _ in range(T):
    N, X = map(int, input().strip().split())
    if X % N == 0:
        print("YES")
    else:
        print("NO")
