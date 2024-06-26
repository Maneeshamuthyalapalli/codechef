def tasty_decisions():
    import sys 
    input = sys.stdin.read 
    data = input().split()
    T = int(data[0])
    results = []
    index = 1 
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index + 1])
        index += 2
        chocolate_tastiness = 2 * X 
        candy_tastiness = 5 * Y   
        if chocolate_tastiness > candy_tastiness:
            results.append("Chocolate")
        elif candy_tastiness > chocolate_tastiness:
            results.append("Candy")
        else:
            results.append("Either")
    for result in results:
        print(result)
if __name__ == "__main__":
    tasty_decisions()
