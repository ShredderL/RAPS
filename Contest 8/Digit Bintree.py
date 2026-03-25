def DigitBintree(S):

    if int(max(S)) - int(min(S)) <= 1:
        return 1
    
    else:
        middle = len(S) // 2
        return DigitBintree(S[ :middle]) + DigitBintree(S[middle: ])


#input
S = input()

bintreeCount = DigitBintree(S)