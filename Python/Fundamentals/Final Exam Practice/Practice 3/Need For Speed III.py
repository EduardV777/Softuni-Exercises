n=int(input())
cars={}
for k in range(0,n):
    carsData=input()
    carsData=carsData.split("|")
    carName=carsData[0]; mileage=int(carsData[1]); fuel=int(carsData[2])
    cars[carName]=[mileage,fuel]
while True:
    command=input()
    if command!="Stop":
        if "Drive" in command:
            command=command.split(" : ")
            distance=int(command[2]); fuel=int(command[3])
            if cars[command[1]][1]>=fuel:
                cars[command[1]][0]+=distance
                cars[command[1]][1]-=fuel
                print(f"{command[1]} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if cars[command[1]][0]>=100000:
                    del cars[command[1]]
                    print(f"Time to sell the {command[1]}!")
            else:
                print("Not enough fuel to make that ride")
        elif "Refuel" in command:
            command=command.split(" : ")
            fuel=int(command[2])
            if fuel+cars[command[1]][1]>75:
                fuel=(75-cars[command[1]][1])
                cars[command[1]][1]+=fuel
            else:
                cars[command[1]][1]+=fuel
            print(f"{command[1]} refueled with {fuel} liters")
        elif "Revert" in command:
            command=command.split(" : ")
            km=int(command[2])
            cars[command[1]][0]-=km
            if not cars[command[1]][0]<10000:
                print(f"{command[1]} mileage decreased by {km} kilometers")
            else:
                cars[command[1]][0]=10000
    else:
        for j in cars:
            print(f"{j} -> Mileage: {cars[j][0]} kms, Fuel in the tank: {cars[j][1]} lt.")
        break
