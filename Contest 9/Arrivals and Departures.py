
def MaxConcurrent(n, timesAndIDs):

    timesAndIDs.sort()
    seen = set()
    currentTotal = 0
    maxConc = 0

    for i in timesAndIDs:
        if i[1] not in seen:
            currentTotal += 1
            seen.add(i[1])
            if currentTotal > maxConc:
                maxConc = currentTotal
        else:
            currentTotal -= 1

    return maxConc

#input
n = int(input().strip())

timesAndIDs = []

for _ in range(n):
    timesAndIDs.append(list(map(int, input().rstrip().split())))

maxConc = MaxConcurrent(n, timesAndIDs)
print(maxConc)