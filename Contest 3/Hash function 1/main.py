
def HashFunction(S) -> int:
    if len(S) > 10000:
        raise ValueError("Input too long.")
    
    runningTotal = 0
    crent = 0
    A = 48271
    M = 2147483647

    for i in S:
        crent = ord(i)
        runningTotal = ((runningTotal+crent) * A) % M

    return runningTotal % 256



#input
S = input("Enter string: ")

hashVal = HashFunction(S)

print(hashVal)