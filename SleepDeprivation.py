
def check_sleep_deprivation(test_cases):
    results = []
    for hours in test_cases:
        if hours < 7:
            results.append("YES")
        else:
            results.append("NO")
    return results 
T = int(input().strip())
test_cases = [] 
for _ in range(T):
    X = int(input().strip())
    test_cases.append(X)
results = check_sleep_deprivation(test_cases)
for result in results:
    print(result)
