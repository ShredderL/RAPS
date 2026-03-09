
def CatOrDog(word):
    catLetters = 0
    dogLetters = 0
    word = word.lower()

    for i in word:
        if i == 'c' or i == 'a' or i == 't':
            catLetters += 1

        elif i == 'd' or i == 'o' or i == 'g':
            dogLetters += 1

    if dogLetters > catLetters:
        result = 'DOG'
    elif catLetters > dogLetters:
        result = 'CAT'
    else:
        result = 'NEITHER'

    return result


#input
word = input()

result = CatOrDog(word)

print(result)