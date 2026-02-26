def TakeSteps(nArray, nSteps, grid):
    currentPos = 0
    seen = {}
    seen[0] = 0


    if nArray > 64 or nSteps > 5 * (10 ** 8):
        raise ValueError("Grid too large.")
    

    for i in range(nSteps):
        rowPos = currentPos // nArray
        colPos = currentPos % nArray

        direction = grid[rowPos][colPos]
         
        if direction == "^":
            rowPos -= 1

        elif direction == "<":
            colPos -= 1
 
        elif direction == ">":
            colPos += 1
 
        elif direction == "v":
            rowPos += 1
        else:
            raise ValueError("Error. Character was not a direction.")

        currentPos = (rowPos * nArray) + colPos

        if currentPos in seen:
            cycleLength = (i+1) - seen[currentPos]
            remainingSteps = nSteps - (i+1)
            remainingEffective = remainingSteps % cycleLength

            for x in range(remainingEffective):
                rowPos = currentPos // nArray
                colPos = currentPos % nArray

                direction = grid[rowPos][colPos]
                        
                if direction == "^":
                    rowPos -= 1

                elif direction == "<":
                    colPos -= 1
                
                elif direction == ">":
                    colPos += 1
                
                elif direction == "v":
                    rowPos += 1
                else:
                    raise ValueError("Error. Character was not a direction.")
                
                currentPos = (rowPos * nArray) + colPos
            
            break

        else:
            seen[currentPos] = i+1

    return currentPos

#input
nArray = int(input("Enter number of rows: ").strip())

nSteps = int(input("Enter number of steps overall: ").strip())

grid = []

for _ in range(nArray):
    grid_item = input("Enter stpes in row: ")
    grid.append(grid_item)

finalCellIndex = TakeSteps(nArray, nSteps, grid)
print(finalCellIndex)