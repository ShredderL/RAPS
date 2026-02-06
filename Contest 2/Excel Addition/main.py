import string

def Base26Add(A, B) -> str:
    carry = 0
    i = len(A) - 1
    j = len(B) - 1
    result = []
    A = A.upper()
    B = B.upper()

    while i >= 0 or j >= 0 or carry > 0:
        if i >= 0:
            a_char = A[i]
        else:
            a_char = 'A'
        if j >= 0:
            b_char = B[j]
        else:
            b_char = 'A'
        
        a_val = ord(a_char) - ord('A')
        b_val = ord(b_char) - ord('A')
        s = a_val + b_val + carry

        digit = s % 26
        carry = s // 26

        digit_char = chr(digit + ord('A'))

        result.append(digit_char)
        i -= 1
        j -= 1


    result.reverse()
    final = "".join(result)



    return final



#input
first_multiple_input = input("Enter strings: ").rstrip().split()

A = first_multiple_input[0]

B = first_multiple_input[1]

sumAB = Base26Add(A, B)

print(sumAB)