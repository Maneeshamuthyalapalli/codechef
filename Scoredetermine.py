def calculate_score(X, N):
    points_per_test_case = X // 10 
    return points_per_test_case * N 
T = int(input())
for _ in range(T):
    X, N = map(int,  input().strip().split())
    print(calculate_score(X, N))
