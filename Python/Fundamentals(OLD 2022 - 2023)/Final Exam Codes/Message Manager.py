cap=int(input())
usrMessages={}
while True:
    command=input()
    if command!="Statistics":
        if "Add" in command:
            command=command.split("=")
            user=command[1]; sent=int(command[2]); received=int(command[3])
            if not user in usrMessages:
                usrMessages[user]=[sent,received]
        elif "Message" in command:
            command=command.split("=")
            sender=command[1]; receiver=command[2]
            if sender in usrMessages and receiver in usrMessages:
                usrMessages[sender][0]+=1
                usrMessages[receiver][1]+=1
                if usrMessages[sender][0]+usrMessages[sender][1]>=cap:
                    del usrMessages[sender]
                    print(f"{sender} reached the capacity!")
                if usrMessages[receiver][0]+usrMessages[receiver][1]>=cap:
                    del usrMessages[receiver]
                    print(f"{receiver} reached the capacity!")
        elif "Empty" in command:
            command=command.split("=")
            user=command[1]
            if user=="All":
                usrMessages={}
            else:
                if user in usrMessages:
                    del usrMessages[user]
    else:
        print(f"Users count: {len(usrMessages)}")
        for j in usrMessages:
            print(f"{j} - {usrMessages[j][0]+usrMessages[j][1]}")
        break
