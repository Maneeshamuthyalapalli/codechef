
def maximum_submissions(X):
    effective_duration = (60 * X) - 5
    return effective_duration // 30 
T = int(input())
for _ in range(T):
    X = int(input())
    print(maximum_submissions(X))
