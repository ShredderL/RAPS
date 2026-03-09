from collections import deque

def ShortestPath(nx, ny, maze):

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = set()
    queue = deque()
    queue.append((0, 0, 1))
    visited.add((0, 0))

    while queue:
        row, col, distance = queue.popleft()
        if row == ny-1 and col == nx-1:
            return print(distance)
        else:
            for r, c in directions:
                newRow = row + r
                newCol = col + c
                if 0 <= newRow < ny and 0 <= newCol < nx:
                    if maze[newRow][newCol] == '.':
                        if (newRow, newCol) not in visited:
                            queue.append((newRow,newCol, distance+1))
                            visited.add((newRow,newCol))

    return -1



#input
first_multiple_input = input().rstrip().split()

nx = int(first_multiple_input[0])

ny = int(first_multiple_input[1])

maze = []

for _ in range(ny):
    maze_item = input()
    maze.append(maze_item)

pathLength = ShortestPath(nx, ny, maze)

print(pathLength)