# cook your dish here
def max_bags(T, test_cases):
    results = []
    for i in range(T):
        X, Y = test_cases[i]
        total_coins = X * Y
        bags = total_coins // 100
        results.append(bags)
    return results
T = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(T)]
results = max_bags(T, test_cases)
for result in results:
    print(result)
