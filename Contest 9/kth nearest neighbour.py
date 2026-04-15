
def KNearestNeighbour(n, k, points):
    distances = []
    x0 = points[0][0]
    y0 = points[0][1]

    for i in range(1, n):
        x = points[i][0]
        y = points[i][1]
        distance = (x - x0)**2 + (y - y0)**2
        distances.append((distance, i))

    distances.sort()

    return distances[k-1][1]


#input
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

points = []

for _ in range(n):
    points.append(list(map(int, input().rstrip().split())))

neighbour = KNearestNeighbour(n, k, points)