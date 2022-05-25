seq1=input(); seq2=input(); n=int(input())
seq1=seq1.split(" "); seq2=seq2.split(" ")
seq1=[int(e) for e in seq1]; seq2=[int(e) for e in seq2]

sequenceSet1=set([]); sequenceSet2=set([])

for k in range(0,len(seq1)):
    sequenceSet1.add(seq1[k])
for k in range(0,len(seq2)):
    sequenceSet2.add(seq2[k])

while n!=0:
    command=input()
    if 'Add First' in command:
        command=command.split(" ")
        del command[1]; del command[0]
        command=[int(e) for e in command]
        for k in range(0,len(command)):
            sequenceSet1.add(command[k])
    elif 'Add Second' in command:
        command = command.split(" ")
        del command[1]; del command[0]
        command = [int(e) for e in command]
        for k in range(0,len(command)):
            sequenceSet2.add(command[k])
    elif 'Remove First' in command:
        command = command.split(" ")
        del command[1]; del command[0]
        command = [int(e) for e in command]
        for k in range(0,len(command)):
            if command[k] in sequenceSet1:
                sequenceSet1.remove(command[k])
    elif 'Remove Second' in command:
        command = command.split(" ")
        del command[1]; del command[0]
        command = [int(e) for e in command]
        for k in range(0,len(command)):
            if command[k] in sequenceSet2:
                sequenceSet2.remove(command[k])
    elif 'Check Subset' in command:
        if sequenceSet1.issubset(sequenceSet2) or sequenceSet2.issubset(sequenceSet1):
            print("True")
        else:
            print('False')
    n-=1


print(', '.join([str(e) for e in  sequenceSet1]))
print(', '.join([str(e) for e in sequenceSet2]))