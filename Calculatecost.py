
def calculate_cost(kms):
    cost_per_km = 10 
    min_distance =300 
    if kms < min_distance:
        return min_distance * cost_per_km
    else:
        return kms * cost_per_km
T = int(input())
for _ in range(T):
    X = int(input())
    print(calculate_cost(X))
