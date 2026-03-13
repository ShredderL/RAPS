
def kaprekarNumbers(p, q):
    kaprekarNums = []

    if 0 >= p >= 100000:
        raise ValueError("Error")
    if 0 >= q >= 100000:
        raise ValueError("Error")

    for i in range(p, q, 1):
        squared = i*i
        squaredStr = str(squared)
        if len(squaredStr) % 2 != 0:
            squaredStr = '0' + squaredStr
        mid = len(squaredStr) // 2
        left = int(squaredStr[:mid])
        right = int(squaredStr[mid:])
        total = 0

        total = left + right

        if total == i:
            kaprekarNums.append(total)

        if not kaprekarNums:
            return print("INVALID RANGE")

    result = ' '.join(str(x) for x in kaprekarNums)

    return print(result)


#input
p = int(input().strip())

q = int(input().strip())

result = kaprekarNumbers(p, q)

print(result)