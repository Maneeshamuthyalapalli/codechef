# cook your dish here
def check_bottles(T, test_cases):
    results = []
    for case in test_cases:
        B1, B2, B3 = case
        empty_count = (1 if B1 == 0 else 0) + (1 if B2 == 0 else 0) + (1 if B3 == 0 else 0)
        if empty_count >= 2:
            results.append("Water filling time")
        else:
            results.append("Not now")
    return results
T = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(T)]
results = check_bottles(T, test_cases)
for result in results:
    print(result)
