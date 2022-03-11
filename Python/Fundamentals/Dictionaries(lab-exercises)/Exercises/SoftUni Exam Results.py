submissions={}
langSubStatistics=[]
while True:
    data=input()
    if data!="exam finished":
        if "banned" in data:
            data=data.split("-")
            submissions[username]="banned"
        else:
            data=data.split("-")
            username=data[0]; lang=data[1]; pts=int(data[2])
            if not username in submissions:
                submissions[username]=[[lang,pts]]
            else:
                langExists=False
                for k in range(0,len(submissions[username])):
                    if submissions[username][k][0]==lang:
                        langExists = True
                        if submissions[username][k][1]<pts:
                            submissions[username][k][1]=pts
                            break
                if langExists==False:
                    submissions[username].append([lang,pts])
            langExists = False
            for k in range(0,len(langSubStatistics)):
                if langSubStatistics[k][0]==lang:
                    langExists=True
                    langSubStatistics[k][1]+=1
                    break
            if langExists==False:
                langSubStatistics.append([lang, 1])
    else:
        print("Results:")
        for j in submissions:
            if submissions[j]=="banned":
                continue
            else:
                for k in range(0,len(submissions[j])):
                    print(f"{j} | {submissions[j][k][1]}")
        print("Submissions:")
        for k in range(0,len(langSubStatistics)):
            print(f"{langSubStatistics[k][0]} - {langSubStatistics[k][1]}")
        break
