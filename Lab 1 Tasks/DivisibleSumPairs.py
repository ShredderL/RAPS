def divisibleSumPairs(n, k, ar) -> int:
    if n < 2 or n > 100 or k < 1 or k > 100:
        raise ValueError("Error, values out of range.")
    if len(ar) != n:
        raise ValueError("n does not match the number of elements in ar.")
    
    numOfPairs = 0

    for x in ar:
        if (x < 1 or x > 100):
            raise ValueError("Error, values outside of range.")


    for i in range(0, len(ar)-1):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                numOfPairs+=1
                #print(numOfPairs)
                #print(f"Current i: {i}, and current j is: {j}.")

    
    return numOfPairs




#input
fmi = input("Enter length of array and integer divisor: ").rstrip().split()

n = int(fmi[0])

k = int(fmi[1])

ar = list(map(int, input("Enter string of numbers: ").rstrip().split()))

print(divisibleSumPairs(n, k, ar))