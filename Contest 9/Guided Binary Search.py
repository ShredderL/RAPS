
def GuidedSearch(N, values, pattern, nSearch):
    low = 0
    high = N

    for i in range(nSearch):
        mid = (low+high)//2
        if pattern % 2 == 1:
            low = mid
        else:
            high = mid
        pattern = pattern //2


    return values[low]



#input
first_multiple_input = input().rstrip().split()

N = int(first_multiple_input[0])

pattern = int(first_multiple_input[1])

nSearch = int(first_multiple_input[2])

values = list(map(int, input().rstrip().split()))

valueFound = GuidedSearch(N, values, pattern, nSearch)