

def LargestFriendGroup(N, M, connections):
    people = list(range(N))

    if N > 1000:
        raise ValueError("Number of individuals too large. ")


    for i in range(0, len(connections), 2):
        a = connections[i]
        b = connections[i+1]

        old = people[b]
        new = people[a]

        for j in range(N):
            if people[j] == old:
                people[j] = new

    largest = 0
    for i in people:
        count = people.count(i)
        if count > largest:
            largest = count

    return largest


#input
first_multiple_input = input().rstrip().split()

N = int(first_multiple_input[0])

M = int(first_multiple_input[1])

connections = list(map(int, input().rstrip().split()))

groupSize = LargestFriendGroup(N, M, connections)
print(groupSize)