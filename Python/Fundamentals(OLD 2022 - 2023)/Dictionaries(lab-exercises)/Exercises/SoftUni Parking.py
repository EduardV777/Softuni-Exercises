n=int(input())
parking={}
for k in range(0,n):
    command=input()
    command = command.split(" ")
    if command[0]=="register":
        doesUserExist=parking.get(command[1],"no")
        if doesUserExist!="no":
            print(f"ERROR: already registered with plate number {parking[command[1]]}")
        else:
            parking[command[1]]=command[2]
            print(f"{command[1]} registered {command[2]} successfully")
    elif command[0]=="unregister":
        doesUserExist=parking.get(command[1],"no")
        if doesUserExist!="no":
            del parking[command[1]]
            print(f"{command[1]} unregistered successfully")
        else:
            print(f"ERROR: user {command[1]} not found")
for j in parking:
    print(f"{j} => {parking[j]}")
