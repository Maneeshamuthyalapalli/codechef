# cook your dish here
def classify_spice_level():
    T = int(input())
    for _ in range(T):
        X = int(input())
        if X < 4:
            print("MILD")
        elif 4 <= X < 7:
            print("MEDIUM")
        else:
            print("HOT")
classify_spice_level()
