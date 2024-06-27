def can_finish_episode_before_exam(X):
    return "YES" if X > 24 else "NO"
T = int(input())
results = []
for _ in range(T):
    X = int(input())
    results.append(can_finish_episode_before_exam(X))
for result in results:
    print(result)
