
def IsPowerThree(x):
    current = x

    while current != 1:
        if current % 3 != 0:
            return "NO"
        current = current//3

    return "YES"


#input
x = int(input("Entrer number: ").strip())

result = IsPowerThree(x)

print(result)