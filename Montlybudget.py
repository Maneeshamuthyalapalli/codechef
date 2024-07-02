def check_budget(T, test_cases):
    results = []
    for i in range(T):
        X, Y = test_cases[i]
        if X >= 30 * Y:
            results.append("YES")
        else:
            results.append("NO")
    return results 
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = check_budget(T, test_cases)
for result in results:
    print(result)
