def can_distribute_equally(A, B):
    return (A + B) % 2 == 0
T = int(input())
results = []
for _ in range(T):
    A, B = map(int, input().split())
    if can_distribute_equally(A, B):
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)
