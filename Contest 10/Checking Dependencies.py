from collections import deque

def CheckDependency(numObjects, numDependencies, A, B, dependencies):
    visited = set()
    visited.add(A)
    queue = deque()
    queue.append(A)

    dependants = []                                     #create and populate list of lists
    for i in range(numObjects):
        dependants.append([])


    for i in range(0, len(dependencies), 2):            #add dependants
        x = dependencies[i]
        y = dependencies[i+1]
        dependants[x].append(y)                         #x leads to y


    while queue:                                        #check if B is reachable from A
        current = queue.popleft()                       #take object to check if it is B
        if current == B:
            return "TRUE"
        
        for i in dependants[current]:                   #get dependants of current and check if they have been visited yet
            if i not in visited:
                queue.append(i)                         #add to queue if not visited
                visited.add(i)

    return "FALSE"                                      #return false if while loop finished and B is not reached




#input
first_multiple_input = input().rstrip().split()

numObjects = int(first_multiple_input[0])

numDependencies = int(first_multiple_input[1])

A = int(first_multiple_input[2])

B = int(first_multiple_input[3])

dependencies = list(map(int, input().rstrip().split()))

result = CheckDependency(numObjects, numDependencies, A, B, dependencies)

print(result)