def ProfitFind(prices: list[int]) -> int:
    owned = False
    profit = 0
    nxtVal = 0
    crentVal = 0

    for i in range(len(prices)-1):
        nxtVal = prices[i+1]
        crentVal = prices[i]

        if not owned and crentVal < nxtVal:
            owned = True
            profit -= crentVal
        elif owned and crentVal > nxtVal:
            owned = False
            profit += crentVal
    if owned:
        profit += prices[-1]
    return profit


prices = list(map(int, input("Please enter a string of prices seperated by spaces: ").split()))
print(f"Maximum profit for {prices} is: ", ProfitFind(prices))
