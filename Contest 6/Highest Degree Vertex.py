


def MaxDegreeVertex(N, M, connections):
    if N >= 500:
        raise ValueError("Too many vertices. ")
    
    if (len(connections)) / 2 != M:
        raise ValueError("Edges do not match vertices. ")


    degree = N * [0]

    for i in connections:
        degree[i] += 1
    return degree.index(max(degree))

#input
first_multiple_input = input().rstrip().split()

N = int(first_multiple_input[0])

M = int(first_multiple_input[1])

connections = list(map(int, input().rstrip().split()))

maxVert = MaxDegreeVertex(N, M, connections)

print(maxVert)