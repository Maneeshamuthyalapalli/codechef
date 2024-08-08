# cook your dish here
def min_flips_to_unify_cards(T, test_cases):
    results = []
    for i in range(T):
        N, X = test_cases[i]
        min_flips = min(X, N - X)
        results.append(min_flips)
    return results
T = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(T)]
results = min_flips_to_unify_cards(T, test_cases)
for result in results:
    print(result)
