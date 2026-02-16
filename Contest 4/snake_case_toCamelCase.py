def SnakeToCamel(snake) -> str:
    output = str
    upperCheck = False
    leadingUnderscore = 0

    newString = snake.strip()
    for i in newString:
        if i == '_':
            leadingUnderscore += 1
        else:
            break

    newString = newString.replace("_", " ")
    newString = newString.title()
    varName = list(newString.split())
    varName[0].lower()
    print(varName, leadingUnderscore)




    return varName




#input

snake = input("Enter variable name: ")

camel = SnakeToCamel(snake)