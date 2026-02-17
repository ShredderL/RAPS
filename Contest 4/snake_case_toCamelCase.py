def SnakeToCamel(snake) -> str:
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

    if varName:
        varName[0] = varName[0].lower()

    prefix = "_" * leadingUnderscore

    varName.insert(0, prefix)

    result = "".join(str(x) for x in varName)

    return result




#input

snake = input("Enter variable name: ")

camel = SnakeToCamel(snake)
print(camel)