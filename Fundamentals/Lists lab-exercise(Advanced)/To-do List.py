notes=""
toDo=[]
while notes!="End":
    notes=input()
    if notes!="End":
        importance=""; task=""; stoppedAt=0
        for j in range(0,len(notes)):
            if notes[j]!="-":
                importance+=notes[j]
            else:
                stoppedAt=j
                break
        for j in range(stoppedAt+1,len(notes)):
            task+=notes[j]
        noteAndImportance=importance+task
        toDo.append(noteAndImportance)
for k in range(0,len(toDo)):
    importanceVal1=""; importanceVal2=""
    for i in range(0,len(toDo[k])):
        if toDo[k][i].isdigit()==True:
            importanceVal1+=toDo[k][i]
        else:
            break
    importanceVal1=int(importanceVal1)
    for j in range(k+1,len(toDo)):
        importanceVal2 = ""
        #calculating importanceVal2 here
        for i in range(0,len(toDo[j])):
            if toDo[j][i].isdigit()==True:
                importanceVal2+=toDo[j][i]
            else:
                break
        importanceVal2=int(importanceVal2)
        #sorting
        if importanceVal1>importanceVal2:
            temp=toDo[j]; toDo[j]=toDo[k]; toDo[k]=temp

for k in range(0,len(toDo)):
    notePieces=[]
    for j in range(0,len(toDo[k])):
        notePieces.append(toDo[k][j])
    if notePieces[0].isdigit()==True:
        notePieces.pop(0)
    if notePieces[0].isdigit()==True:
        notePieces.pop(0)
    toDo[k]="".join(notePieces)
print(toDo)
