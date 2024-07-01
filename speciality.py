def most_active_role(X, Y, Z):
    if X > Y and X > Z:
        return "Setter"
    elif Y > X and Y > Z:
        return "Tester"
    else:
        return "Editorialist"
T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    print(most_active_role(X, Y, Z))
