R1, R2 = map(int, input().strip().split())
D1, D2 = map(int, input().strip().split())
final_rating_dominater = R1 + D1
final_rating_everule = R2 + D2
if final_rating_dominater > final_rating_everule:
    print("Dominater")
else:
    print("Everule")
