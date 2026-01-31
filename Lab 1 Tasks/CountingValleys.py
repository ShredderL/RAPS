def countingValleys(steps, path):
    #check valid input length and matching string
    if len(path) < 2 or len(path) != steps or (len(path) % 2 == 1):
        raise ValueError("Invalid path length (too short or instructions don't match length).")
    
    #values
    crntAlt = 0
    seaLvl = 0
    valleys = 0
    path = path.upper()
    options = ["U","D"]
    inValley = False

    for i in range(0, len(path)):
        if path[i] not in options:                                                         #Check steps valid
            raise ValueError("Path instructions contained invalid value.")
        

        #alt logic
        if path[i] == "U":
            crntAlt += 1
        if path[i] == "D":
            crntAlt -= 1


        #valley logic
        if crntAlt >= seaLvl:
            inValley = False

        if not inValley:
            if crntAlt < seaLvl:
                valleys += 1
                inValley = True
            
    if crntAlt != seaLvl:
        raise ValueError("Invalid hike, did not start and end at sea level.")
    return valleys




#input
steps = int(input("Please enter number of steps: ").strip())
path = str(input("Please enter a steps: "))
print(countingValleys(steps, path))