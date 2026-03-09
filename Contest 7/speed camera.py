
def Tickets(nLines, data):
    sTickets = 0
    cars = dict()


    for i in data:
        parts = i.split()
        timeInSeconds = (int(parts[1])*3600) + (int(parts[2])*60) + (int(parts[3]))
        if parts[0] not in cars:
            cars[parts[0]] = (timeInSeconds)
        else:
            timeDifference = (timeInSeconds - cars[parts[0]]) / 3600
            speed = 0.5/timeDifference
            if speed >= 55:
                sTickets +=1

    return sTickets


#input
nLines = int(input().strip())

data = []

for _ in range(nLines):
    data_item = input()
    data.append(data_item)

ticketCount = Tickets(nLines, data)