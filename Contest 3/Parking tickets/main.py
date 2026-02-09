def ParkingTickets(numEvents, registrations, times) -> int:
    ticketsIssued = 0
    cars = {}
    numOfCars = 0

    #constraints
    if numEvents >= 500:
        raise ValueError("Too many events.")
    if len(registrations) != numEvents and len(times) != numEvents:
        raise ValueError("Number of events, registrations, and times do not match.")

    
    for i in range(numEvents):
        if registrations[i] in cars and cars[registrations[i]]["ticketIssued"] == True:
            if cars[registrations[i]]["inCarPark"]:
                cars[registrations[i]]["inCarPark"] = False
                numOfCars-=1
            elif not cars[registrations[i]]["inCarPark"]: 
                cars[registrations[i]]["inCarPark"] = True
                numOfCars+=1
            
            continue


        elif registrations[i] not in cars:
            cars[registrations[i]] = {"arrivalTime": times[i], "inCarPark": True, "ticketIssued": False}
            numOfCars+=1

        elif registrations[i] in cars:

            if cars[registrations[i]]["inCarPark"]:
                cars[registrations[i]]["departureTime"] = times[i]
                numOfCars-=1
                cars[registrations[i]]["inCarPark"] = False

                if cars[registrations[i]]["departureTime"] - cars[registrations[i]]["arrivalTime"] > 60:
                    cars[registrations[i]]["ticketIssued"] = True
                    ticketsIssued += 1


            
            elif not cars[registrations[i]]["inCarPark"]:
                cars[registrations[i]]["inCarPark"] = True
                cars[registrations[i]]["arrivalTime"] = times[i]
                numOfCars+=1

                if cars[registrations[i]]["arrivalTime"] - cars[registrations[i]]["departureTime"] < 60:
                    cars[registrations[i]]["ticketIssued"] = True
                    ticketsIssued +=1

            #else:
                #print("Error somewhere, num events: ", numEvents[i], "reg: ", registrations[i], "time: ",times[i])

    if numOfCars != 0:
        raise ValueError("Error with input, car park not empty.")


    return ticketsIssued


#input
n = int(input("Enter number of events: ").strip())

registrations = input("Enter registrations: ").rstrip().split()

times = list(map(int, input("Enter times each car stayed for: ").rstrip().split()))

tickets = ParkingTickets(n, registrations, times)

print(tickets)