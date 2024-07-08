
def check_fever(test_cases):
    results = []
    for temp in test_cases:
        if temp > 98:
            results.append("YES")
        else:
            results.append("NO")
    return results 
T = int(input().strip())
test_cases = []
for _ in range(T):
    X = int(input().strip())
    test_cases.append(X)
results = check_fever(test_cases)
for result in results:
    print(result)
