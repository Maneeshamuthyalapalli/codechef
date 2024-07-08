# cook your dish here
def calculate_extra_seats(test_cases):
    results = [] 
    for X, Y in test_cases:
        if Y > X:
            results.append(Y - X)
        else:
            results.append(0)
    return results 
T = int(input().strip())
test_cases = [] 
for _ in range(T):
    X, Y = map(int, input().strip().split())
    test_cases.append((X, Y))
results = calculate_extra_seats(test_cases)
for result in results:
    print(result)
            
