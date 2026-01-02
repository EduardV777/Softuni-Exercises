companies={}
while True:
    data=input()
    if data!="End":
        data=data.split(" -> ")
        if data[0] in companies:
            if not data[1] in companies[data[0]]:
                companies[data[0]].append(data[1])
        else:
            companies[data[0]]=[data[1]]
    else:
        for j in companies:
            print(f"{j}")
            for k in range(0,len(companies[j])):
                print(f"-- {companies[j][k]}")
        break
