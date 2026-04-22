
def PathLength(numVert, numEdge, v0, v1, edges):
    connected = []                                     #create and populate list of lists
    for i in range(numVert):
        connected.append([])

    for i in range(0, len(edges), 3):
        a = edges[i]
        b = edges[i+1]
        w = edges[i+2]
        connected[a].append((b, w))                     #store neighbour and weight
        connected[b].append((a, w))                     #undirected so both ways


    pass



#input
first_multiple_input = input().rstrip().split()

numVert = int(first_multiple_input[0])

numEdge = int(first_multiple_input[1])

v0 = int(first_multiple_input[2])

v1 = int(first_multiple_input[3])

edges = list(map(int, input().rstrip().split()))

length = PathLength(numVert, numEdge, v0, v1, edges)