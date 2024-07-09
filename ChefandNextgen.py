T = int(input())
for _ in range(T):
    A, B, X, Y = map(int, input().split())
    required_power = A * B 
    generated_power = X * Y
    if generated_power >= required_power:
        print("YES")
    else:
        print("NO")
