
def calculate_fine(speed):
    if speed <= 70:
        return 0 
    elif speed <=100:
        return 500
    else:
        return 2000
T = int(input())
for _ in range(T):
    X = int(input())
    fine = calculate_fine(X)
    print(fine)
