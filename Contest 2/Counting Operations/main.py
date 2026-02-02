def OperationCount(A, B) -> int:
    numOfOp = 0
    X = A
    if A > B:
        return ValueError("First number must be less than second number.")
    
    while A != B:
        if A*X <= B:
            A=A*X
        
        elif A+X <= B:
            A=A+X

        else:
            A=A+1
            
        numOfOp += 1
            


    return numOfOp







#input
first_multiple_input = input("Enter: ").rstrip().split()

A = int(first_multiple_input[0])

B = int(first_multiple_input[1])

result = OperationCount(A, B)

print(result)