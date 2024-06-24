def did_chef_dominate(X, Y):
    if X >= 2 * Y:
        return "Yes"
    else:
        return "No"
X, Y = map(int, input().strip().split())
print(did_chef_dominate(X, Y))
