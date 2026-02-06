
def Mode(n, values):
    if n < 1 or n > 10000:
        raise ValueError("Error, values outside range.")
    
    list = sorted(values)
    count = 1
    leader = 0
    highscore = 0
    print(list)
    multimodal = False

    for i in range(len(list) - 1):
        if list[i] == list[i+1]:
            count += 1
            if count > highscore:
                leader = list[i]
                highscore = count
                multimodal = False
            elif count == highscore:
                multimodal = True

        elif list[i] != list[i+1]:
            count = 1


    if not multimodal: return leader
    else: return -1



#input
n = int(input("Enter amount of values: ").strip())

values = []

for _ in range(n):
    values_item = int(input("Enter value: ").strip())
    values.append(values_item)

mode = Mode(n, values)
print(mode)