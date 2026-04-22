
def StationaryCount(numValues, values):
    result = 0

    copy = sorted(values)

    for i in range(0, numValues):
        if values[i] == copy[i]:
            result+=1

    return result


#input
numValues = int(input().strip())

values = list(map(int, input().rstrip().split()))

count = StationaryCount(numValues, values)

print(count)