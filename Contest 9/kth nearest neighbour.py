
def KNearestNeighbour(n, k, points):
    distances = {}



    pass


#input
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

points = []

for _ in range(n):
    points.append(list(map(int, input().rstrip().split())))

neighbour = KNearestNeighbour(n, k, points)