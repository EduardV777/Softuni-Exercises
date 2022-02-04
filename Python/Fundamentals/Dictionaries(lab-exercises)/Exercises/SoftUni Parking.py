parkedCars={}
n=int(input())
for k in range(0,n):
    command=input()
    if "register" in command and not "unregister" in command:
        userData=command.split(" ")
        alreadyRegistered=False
        for j in parkedCars:
            if userData[1]==j:
                print(f"ERROR: already registered with plate number {parkedCars[j]}")
                alreadyRegistered=True
                break
        if alreadyRegistered==False:
            parkedCars[userData[1]]=userData[2]
            print(f"{userData[1]} registered {userData[2]} successfully")
    elif "unregister" in command:
        userData=command.split(" ")
        userNotFound=False
        for j in parkedCars:
            if userData[1]==j:
                userNotFound=False
                print(f"{j} unregistered successfully")
                del parkedCars[j]
                break
            else:
                userNotFound=True
        if userNotFound==True:
            print(f"ERROR: user {userData[1]} not found")
for j in parkedCars:
    print(f"{j} => {parkedCars[j]}")
