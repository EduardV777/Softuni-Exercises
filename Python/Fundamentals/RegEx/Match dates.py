import re
dateScheme=re.compile(r"\b(\d{2})([-./])([A-Z]{1}[a-z]{2})\2(\d{4})\b")
dates=input()
res=dateScheme.findall(dates)

for k in range(0,len(res)):
    temp=[]
    for j in range(0,len(res[k])):
        temp.append(res[k][j])
    res[k]=temp; del res[k][1]

for k in range(0,len(res)):
    print(f"Day: {res[k][0]}, Month: {res[k][1]}, Year: {res[k][2]}")
