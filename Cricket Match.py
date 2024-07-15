# Read the number of test cases
T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    max_possible_runs = 36 * M
    if N <= max_possible_runs:
        print("YES")
    else:
        print("NO")
