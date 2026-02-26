def findWords(words) -> list[str]:
    letters = {}

    completeWords = []

    topRow = "qwertyuiopQWERTYUIOP"
    midRow = "asdfghjklASDFGHJKL"
    botRow = "zxcvbnmZXCVBNM"

    for i in topRow:
        letters[i] = {"topRow": True, "midRow": False, "botRow": False}

    for i in midRow:
        letters[i] = {"topRow": False, "midRow": True, "botRow": False}

    for i in botRow:
        letters[i] = {"topRow": False, "midRow": False, "botRow": True}


    for i in words:
        add = True
        for char in i:
            if char in letters and letters[char]["topRow"]:
                continue
            elif char not in topRow:
                add = False
        
        if add:
            completeWords.append(i)

    for i in words:
        add = True
        for char in i:
            if char in letters and letters[char]["midRow"]:
                continue
            elif char not in midRow:
                add = False
        
        if add:
            completeWords.append(i)

    for i in words:
        add = True
        for char in i:
            if char in letters and letters[char]["botRow"]:
                continue
            elif char not in botRow:
                add = False
        
        if add:
            completeWords.append(i)
            

    return completeWords



#input


words = input("Enter words:").split(" ")

result = findWords(words)

print(result)