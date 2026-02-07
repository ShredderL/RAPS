def UniquePairs(n, values) -> int:
    if n < 0 or n > 10000:
        raise ValueError("Error.")
    
    uniqueVals = list(set(values))
    sizeofUnique = len(uniqueVals)
    numOfPairs = int((sizeofUnique * (sizeofUnique-1))/2)

    return numOfPairs


#input
n = int(input("Enter number of values: ").strip())

values = []

for _ in range(n):
    values_item = int(input("Enter value: ").strip())
    values.append(values_item)

count = UniquePairs(n, values)
print(count)