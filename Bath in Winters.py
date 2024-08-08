# cook your dish here
def max_people_bath(T, test_cases):
    results = []
    for i in range(T):
        X, Y = test_cases[i]
        if Y == 0:
            results.append(0)
        else:
            water_per_person = 2 * Y
            max_people = X // water_per_person
            results.append(max_people)
    return results
T = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(T)]
results = max_people_bath(T, test_cases)
for result in results:
    print(result)
