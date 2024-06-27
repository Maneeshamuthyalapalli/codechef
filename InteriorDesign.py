T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    cost_style1 = x1 + y1 
    cost_style2 = x2 + y2 
    min_cost = min(cost_style1, cost_style2)
    print(min_cost)
