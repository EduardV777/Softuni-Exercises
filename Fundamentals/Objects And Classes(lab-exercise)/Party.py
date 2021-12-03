class Party:
    def __init__(self):
        self.people=[]
command=""
party1=Party()
for k in range(0,2):
    party1.people.append(list())
n=0
while command!="End":
    command=input()
    if command!="End":
        party1.people[0].append(command)
        n+=1
    else:
        party1.people[1] = str(n)
print(f"Going: {', '.join(party1.people[0])}\nTotal: {party1.people[1][0]}")
