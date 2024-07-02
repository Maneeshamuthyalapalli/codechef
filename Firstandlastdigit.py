def first_and_last_digit_sum(N):
    last_digit = N % 10 
    first_digit = N 
    while first_digit >= 10:
        first_digit //= 10 
    return first_digit + last_digit 
T = int(input())
for _ in range(T):
    N = int(input())
    result = first_and_last_digit_sum(N)
    print(result)
