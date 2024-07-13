def can_divide_pizza(T, test_cases):
    results = []
    for N in test_cases:
        if N == 1 or N % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    return results
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]
results = can_divide_pizza(T, test_cases)
for result in results:
    print(result)
