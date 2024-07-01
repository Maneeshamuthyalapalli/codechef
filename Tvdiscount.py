def find_cheaper_tv(A, B, C, D):
    price1 = A - C 
    price2 = B - D 
    if price1 < price2:
        return "First"
    elif price1 > price2:
        return "Second"
    else:
        return "Any"
T = int(input())
for _ in range(T):
    A, B, C, D = map(int, input().split())
    print(find_cheaper_tv(A, B, C, D))
