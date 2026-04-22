
def CatOrDog2(word):
    word = word.lower()
    catMax = 0
    dogMax = 0
    catCurrent = 0
    dogCurrent = 0
    catLetters = {"c","a","t"}
    dogLetters = {"d","o","g"}

    for i in word:
        if i in catLetters:                 #if cat letter increase cat letter count, reset dog, and update max
            catCurrent += 1
            if catCurrent > catMax:
                catMax = catCurrent
            dogCurrent = 0
        elif i in dogLetters:               #if dog letter increase dog letter count, reset cat, and update max
            dogCurrent += 1
            if dogCurrent > dogMax:
                dogMax = dogCurrent
            catCurrent = 0
        else:                               #otherwise reset both counts
            catCurrent = 0
            dogCurrent = 0

    if catMax > dogMax:
        return "CAT"
    elif dogMax > catMax:
        return "DOG"
    else:
        return "NEITHER"



#input
word = input()

result = CatOrDog2(word)
print(result)