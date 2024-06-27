def max_minus_min(test_cases):
    results = []
    for case in test_cases:
        A, B, C = case 
        maximum = max(A, B, C)
        minimum = min(A, B, C)
        difference = maximum - minimum 
        results.append(difference)
    return results 
T = int(input())
test_cases = [] 
for _ in range(T):
    A, B, C = map(int, input().split())
    test_cases.append((A, B, C))
results =max_minus_min(test_cases)
for result in results:
    print(result)
