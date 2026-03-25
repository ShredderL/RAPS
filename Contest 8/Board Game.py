def CountWays(m, n):
    if m>20 or n>100:
        raise ValueError("Numbers out of range. ")


    ways = [0] * n
    ways[0] = 1



    for i in range(1, n):
        for j in range(1,m+1):
            if i - j >=0:
                ways[i] += ways[i-j]


    return ways[n-1]






#input
first_multiple_input = input().rstrip().split()

m = int(first_multiple_input[0])

n = int(first_multiple_input[1])

count = CountWays(m, n)