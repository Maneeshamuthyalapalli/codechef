# cook your dish here
import math
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    factorial_result = math.factorial(n)
    results.append(factorial_result)
for result in results:
    print(result)

