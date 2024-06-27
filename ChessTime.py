def max_chess_games(T, test_cases):
    results = []
    for N in test_cases:
        results.append(3 * N)
    return results 
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]
results = max_chess_games(T, test_cases)
for result in results:
    print(result)
