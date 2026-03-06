from collections import deque



def DegreeOfSeparation(N, M, connections, A, B):

    connected = []
    steps = deque()
    visited = set()

    if A == B:
        return 0

    for i in range(N):
        connected.append([])

    for i in range(0, len(connections), 2):
        a = connections[i]
        b = connections[i+1]

        connected[a].append(b)
        connected[b].append(a)

    
    visited.add(A)
    for i in connected[A]:
        steps.append((i, 1))
        visited.add(i)

    while steps:
        person, distance = steps.popleft()
        if person == B:
            return distance
        else:
            for i in connected[person]:
                if i not in visited:
                    steps.append((i, distance + 1))
                    visited.add(i)

    return -1



#input
first_multiple_input = input().rstrip().split()

N = int(first_multiple_input[0])

M = int(first_multiple_input[1])

connections = list(map(int, input().rstrip().split()))

second_multiple_input = input().rstrip().split()

A = int(second_multiple_input[0])

B = int(second_multiple_input[1])

degree = DegreeOfSeparation(N, M, connections, A, B)

print(degree)
