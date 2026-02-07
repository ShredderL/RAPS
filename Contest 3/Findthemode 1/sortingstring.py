
def Mode(n, values):
    if n < 1 or n > 10000:
        raise ValueError("Error, values outside range.")
    
    sortVal = sorted(values)
    count = 1
    leader = sortVal[0]
    highscore = 1

    if n == 1 and sortVal[0] <0:
        raise ValueError("Negative numbers not allowed.")
    
    if n == 1: multimodal = False 
    else: multimodal = True


    for i in range(len(sortVal) - 1):
        if sortVal[i] < 0 or sortVal[i+1] < 0:
            raise ValueError("Negative numbers not allowed.")


        if sortVal[i] == sortVal[i+1]:
            count += 1
            if count > highscore:
                leader = sortVal[i]
                highscore = count
                multimodal = False
            elif count == highscore:
                multimodal = True

        elif sortVal[i] != sortVal[i+1]:

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