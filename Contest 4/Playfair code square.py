from string import ascii_uppercase


def PlayfairCode(plainText, codePhrase):
    grid = []
    currentRow = []
    letters = []
    plainTextPairs = []
    encoded = []
    positions = {}
    codePhrasePrepped = ""
    rowPos=0
    colPos=0
    codePhrase = codePhrase.upper()
    codePhrase = codePhrase.replace("J", "I")
    plainText = plainText.upper()
    plainText = plainText.replace("J", "I")
    i = 0



    #plain text logic
    while i < len(plainText)-1:
        if plainText[i] == "J":
            char = "I"
            if plainText[i+1] == "J":
                nextChar = "I"
            else:
                nextChar = plainText[i+1]
        
        else:
            char = plainText[i]
            nextChar = plainText[i+1]

        if char != nextChar:
            currentPair = "".join(char + nextChar)
            plainTextPairs.append(currentPair)
            i += 2
        else:
            currentPair = "".join(char + "X")
            plainTextPairs.append(currentPair)
            i += 1

        
    if i == len(plainText) - 1:
        lastChar = plainText[i]
        if lastChar == "J":
            lastChar = "I"
        plainTextPairs.append(lastChar + "X")



    #codephrase logic
    for char in codePhrase:
        if char == "J" and char not in letters:
            letters.append("I")

        elif char not in letters:
            letters.append(char)

    for char in ascii_uppercase:
        if char not in letters and char != "J":
            letters.append(char)
    
    codePhrasePrepped = "".join(letters)

    for char in codePhrasePrepped:
        currentRow.append(char)
        positions[char] = (rowPos, colPos)
        colPos += 1
        if len(currentRow) == 5:
            grid.append(currentRow)
            currentRow = []
            rowPos += 1
            colPos = 0


    for pair in plainTextPairs:

        row1, col1 = positions[pair[0]]
        row2, col2 = positions[pair[1]]

        if row1 == row2:
            newA = grid[row1][(col1 + 1) % 5]
            newB = grid[row2][(col2 + 1) % 5]
        elif col1 == col2:
            newA = grid[(row1 + 1) % 5][col1]
            newB = grid[(row2 + 1) % 5][col2]
        else:
            newA = grid[row1][col2]
            newB = grid[row2][col1]

        encodedPair = newA + newB
        encoded.append(encodedPair)
            

    encodedSentence = "".join(str(x) for x in encoded)

    return encodedSentence




#input
first_multiple_input = input("Enter plain text and code phrase: ").rstrip().split()

plainText = first_multiple_input[0]

codePhrase = first_multiple_input[1]

cipherText = PlayfairCode(plainText, codePhrase)
print(cipherText)