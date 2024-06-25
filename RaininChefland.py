def categorize_rainfall(T, rainfall_rates):
    results = [] 
    for X in rainfall_rates:
        if X < 3:
            results.append("LIGHT")
        elif 3 <= X < 7:
            results.append("MODERATE")
        else:
            results.append("HEAVY")
    return results 
T = int(input())
rainfall_rates = [int(input()) for _ in range(T)]
results = categorize_rainfall(T, rainfall_rates)
for result in results:
    print(result)
