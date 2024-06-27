def can_go_on_ride(X, H):
    return "YES" if X >= H else "NO"
T = int(input())
for _ in range(T):
    X, H = map(int, input().split())
    print(can_go_on_ride(X, H))
