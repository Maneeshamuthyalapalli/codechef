# cook your dish here
def mahasena(T, weapons):
    even_count = 0
    odd_count = 0
    for weapon in weapons:
        if weapon % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count > odd_count:
        return "READY FOR BATTLE"
    else:
        return "NOT READY"
T = int(input().strip())
weapons = list(map(int, input().strip().split()))
print(mahasena(T, weapons))
