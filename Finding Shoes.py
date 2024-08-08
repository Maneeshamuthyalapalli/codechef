T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    
    if M >= N:
        extra_shoes = N
    else:
        extra_shoes = 2 * N - M
    print(extra_shoes)
