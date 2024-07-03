def min_operations(T, cases):
    results = [] 
    for A, B in cases:
        if A % 3 == 0 or B % 3 == 0:
            results.append(0)
        elif A % 3 == B % 3:
            results.append(1)
        else:
            results.append(2)
    return results
import sys 
input = sys.stdin.read 
data = input().split()
T = int(data[0])
cases = [(int(data[2*i + 1]), int(data[2*i + 2 ])) for i in range(T)] 
results = min_operations(T, cases)
for result in results:
    print(result)
