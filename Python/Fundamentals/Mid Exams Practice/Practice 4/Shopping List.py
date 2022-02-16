groceries=input()
groceries=groceries.split("!")
while True:
    command=input()
    if command!="Go Shopping!":
        if "Urgent" in command:
            command=command.split(" ")
            item=command[1]
            if '!'.join(groceries).find(item)==-1:
                groceries.insert(0,item)
        elif "Unnecessary" in command:
            command=command.split(" ")
            item=command[1]
            if '!'.join(groceries).find(item) != -1:
                ind=groceries.index(item)
                del groceries[ind]
        elif "Correct" in command:
            command=command.split(" ")
            oldItem=command[1]; newItem=command[2]
            if '!'.join(groceries).find(oldItem) != -1:
                ind=groceries.index(oldItem)
                groceries[ind]=newItem
        elif "Rearrange" in command:
            command=command.split(" ")
            item=command[1]
            if '!'.join(groceries).find(item) != -1:
                ind=groceries.index(item)
                del groceries[ind]
                groceries.append(item)
    else:
        print(', '.join(groceries))
        break

