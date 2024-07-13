# cook your dish here
def total_working_hours(T, test_cases):
    results = []
    for i in range(T):
        X, Y = test_cases[i]
        total_hours = (4 * X) + Y
        results.append(total_hours)
    return results
T = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(T)]
results = total_working_hours(T, test_cases)
for result in results:
    print(result)
