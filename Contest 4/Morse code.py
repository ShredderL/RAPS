def MorseEquivalent(A, B):
    morseAlphabet = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..'}
    
    morseA = []
    morseB = []


    for i in A:
        if i in morseAlphabet:
            morseA.append(morseAlphabet[i])
        else:
            raise ValueError("Character not a letter.")

    for i in B:
        if i in morseAlphabet:
            morseB.append(morseAlphabet[i])
        else:
            raise ValueError("Character not a letter.")

    Astring = "".join(morseA)
    Bstring = "".join(morseB)


    if Astring == Bstring:
        Equivalent = "TRUE"
    else:
        Equivalent = "FALSE"

    print(Equivalent)

    return



#input
first_multiple_input = input("Enter: ").rstrip().split()

A = first_multiple_input[0]

B = first_multiple_input[1]

output = MorseEquivalent(A, B)
print(output)