# cook your dish here
def can_design_flag(A, B, C):
    max_strips = max(A, B, C)
    total_strips = A + B + C
    if max_strips > (total_strips + 1) // 2:
        return "NO"
    else:
        return "YES"
T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    print(can_design_flag(A, B, C))
