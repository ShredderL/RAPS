
def IsValidSudoku(s):
    grid = []

    for i in range(0, 81, 9):
        grid.append(s[i:i+9])
    
    for i in range(0, 9):
        row = set()
        col = set()
        for j in grid[i]:
            if j not in row:
                row.add(j)
            else:
                return "INVALID"
        for x in range(0, 9):
            char = grid[x][i]
            if char not in col:
                col.add(char)
            else:
                return "INVALID"
            
    for gridRow in range(0, 9, 3):
        for gridCol in range(0, 9, 3):
            box = set()
            for i in range(gridRow, gridRow+3):
                for j in range(gridCol, gridCol+3):
                    number = grid[i][j]
                    if number not in box:
                        box.add(number)
                    else:
                        return "INVALID"

    return "VALID"


#input
s = input()

result = IsValidSudoku(s)