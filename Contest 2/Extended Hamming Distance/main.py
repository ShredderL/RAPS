def HammingDistance(A, B) -> int:
    numDC = 0

    if len(A) > 50 or len(B) > 50:
        raise ValueError("String length too long.")
    
    diff = abs(len(A)-len(B))

    if len(A) > len(B):
        B += "!" * diff
    elif len(B) > len(A):
        A += "!" * diff
    
    for i in range(len(A)):
        if A[i] != B[i]:
            numDC += 1


    return numDC




#input
first_multiple_input = input("Enter strings: ").rstrip().split()

A = first_multiple_input[0]

B = first_multiple_input[1]

distance = HammingDistance(A, B)

print(distance)