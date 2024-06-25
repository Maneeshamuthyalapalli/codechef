def determine_training_session(X, Y):
    if X > Y:
        print("FREEKICK")
    else:
        print("PENALTY")
X, Y = map(int, input().split())
determine_training_session(X, Y)
