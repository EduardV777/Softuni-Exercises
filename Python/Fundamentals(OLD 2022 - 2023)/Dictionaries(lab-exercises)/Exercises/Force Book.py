forceBook={}
while True:
    command=input()
    if command!="Lumpawaroo":
        if "|" in command:
            command=command.split(" | ")
            isThereSuchUser=False
            for j in forceBook:
                for k in range(0,len(forceBook[j])):
                    if forceBook[j][k]==command[1]:
                        isThereSuchUser=True
                        break
                if isThereSuchUser == True:
                    break
            if isThereSuchUser==True:
                continue
            else:
                if command[0] in forceBook:
                    forceBook[command[0]].append(command[1])
                else:
                    forceBook[command[0]]=[command[1]]
        elif "->" in command:
            command=command.split(" -> ")
            isThereSuchUser=False
            for j in forceBook:
                for k in range(0,len(forceBook[j])):
                    if forceBook[j][k]==command[0]:
                        isThereSuchUser=True
                        del forceBook[j][k]
                        break
                if isThereSuchUser==True:
                    break
            if not command[1] in forceBook:
                forceBook[command[1]]=[command[0]]
            else:
                forceBook[command[1]].append(command[0])
            print(f"{command[0]} joins the {command[1]} side!")
    else:
       for j in forceBook:
           if len(forceBook[j])!=0:
               print(f"Side: {j}, Members: {len(forceBook[j])}")
               for k in range(0,len(forceBook[j])):
                   print(f"! {forceBook[j][k]}")
           else:
             continue
       break
