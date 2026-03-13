from collections import Counter

def canConstruct(ransomNote, magazine):
    result = True

    letters = Counter(magazine)

    for i in ransomNote:
        if letters[i] == 0:
            result = False
            return result
        else:
            letters[i] -= 1

    return result




#input
ransomNote = str(input("Enter String: "))

magazine = str(input("Enter String: "))

print(canConstruct(ransomNote, magazine))
