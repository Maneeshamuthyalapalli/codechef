def can_give_party(T, test_cases):
    results = []
    for case in test_cases:
        N, X, K = case 
        total_cost = N * X 
        if total_cost <= K:
            results.append("YES")
        else:
            results.append("NO")
    return results 
T = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(T)]
results = can_give_party(T, test_cases)
for result in results:
    print(result)
