T = int(input().strip())
for _ in range(T):
    X, A, B = map(int, input().strip().split())
    total_score = A + B * 2
    if total_score >= X:
        print("Qualify")
    else:
        print("NotQualify")
