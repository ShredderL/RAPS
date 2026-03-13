
def ValidBrackets(s):
    bracketPairs = {')': '(', '}': '{', ']': '['}
    stack = []


    for i in s:
        if i not in bracketPairs:
            stack.append(i)
        else:
            if stack and stack[-1] == bracketPairs[i]:
                stack.pop()
            else:
                return "INVALID"
    if not stack: return "VALID"
    else: return "INVALID"



#input
s = input()

result = ValidBrackets(s)

print(result)