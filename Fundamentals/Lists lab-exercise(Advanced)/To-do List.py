notesList=[]
while True:
    note=input()
    if note!="End":
        note=note.split("-")
        notesList.append(note)
    else:
        break
notesList=sorted(notesList, key=lambda x: x[0])
for k in range(0,len(notesList)):
    notesList[k]=notesList[k][1]
print(notesList)
