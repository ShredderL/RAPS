def ValidWalk(S: str) -> str:
    alph = "abcdefghijklmnopqrstuvwxyz"
    S = S.lower()

    if len(S) <= 1:
        return "VALID"

    for pos in range(1, len(S)):
        prev = S[pos - 1]
        cur = S[pos]

        # safety: if input contains non-letters
        if prev not in alph or cur not in alph:
            return "INVALID"

        prev_i = alph.index(prev)
        cur_i = alph.index(cur)

        if abs(cur_i - prev_i) != 1:
            return "INVALID"

    return "VALID"


#input
S = str(input("Please enter a string: "))
print(f"String is: {S}")
print(ValidWalk(S))
