def LeaderboardPosition(nLines, scoreData, name):
    scores = {}
    result = 1
    for i in scoreData:
        x = i.split()
        scores[x[0]] = int(x[1])
    

    for i in scores:
        if scores[i] < scores[name]:
            result += 1

    return result




#input
first_multiple_input = input().rstrip().split()

nLines = int(first_multiple_input[0])

name = first_multiple_input[1]

data = []

for _ in range(nLines):
    data_item = input()
    data.append(data_item)

position = LeaderboardPosition(nLines, data, name)

print(position)