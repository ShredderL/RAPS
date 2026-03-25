from itertools import combinations

def PathCount(nx, ny, numObstacles, k, obstacles):
    maxPaths = 0

    for combo in combinations(obstacles, k):
        destroyed = combo
        paths = [[0] * nx for i in range(ny)]
        paths[0][0] = 1
        for i in range(1, ny):
            if [0,i] in obstacles and [0,i] not in destroyed:
                paths[i][0] = 0
            else:
                paths[i][0] = paths[i-1][0]

        for i in range(1, nx):
            if [i,0] in obstacles and [i,0] not in destroyed:
                paths[0][i] = 0
            else:
                paths[0][i] = paths[0][i-1]


        for i in range(1, ny):
            for j in range(1, nx):
                if [j, i] in obstacles and [j, i] not in destroyed:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        maxPaths = max(maxPaths, paths[ny-1][nx-1])



    return maxPaths



#input
first_multiple_input = input().rstrip().split()

nx = int(first_multiple_input[0])

ny = int(first_multiple_input[1])

numObstacles = int(first_multiple_input[2])

k = int(first_multiple_input[3])

obstacles = []

for _ in range(numObstacles):
    obstacles.append(list(map(int, input().rstrip().split())))

pathCount = PathCount(nx, ny, numObstacles, k, obstacles)