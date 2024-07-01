def can_eat_all_bread(N, M, K):
    if M * K >= N:
       return "Yes"
    else:
        return "No"
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    print(can_eat_all_bread(N, M, K))
        
