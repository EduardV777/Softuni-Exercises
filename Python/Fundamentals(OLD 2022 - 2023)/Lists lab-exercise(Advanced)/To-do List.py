notes=[0]*10
while True:
    command=input()
    if command!="End":
        tokens=command.split("-")
        priority=int(tokens[0])-1
        note=tokens[1]
        notes.pop(priority)
        notes.insert(priority, note)
    else:
        break
res=[element for element in notes if element != 0]
print(res)
