values=input()
values=values.split(" "); values=[int(e) for e in values]
while True:
    command=input()

    if command!="end":
        if "swap" in command:
            command=command.split(" ")
            ind1=int(command[1]); ind2=int(command[2])
            temp=values[ind1]
            values[ind1]=values[ind2]
            values[ind2]=temp
        elif "multiply" in command:
            command=command.split(" ")
            ind1 = int(command[1]); ind2 = int(command[2])
            values[ind1]=values[ind1]*values[ind2]
        elif "decrease" in command:
            values=[e-1 for e in values]
    else:
        break

values=[str(e) for e in values]
print(', '.join(values))
