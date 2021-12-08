students={}
while True:
    stringLine=input()
    if ":" in stringLine:
        k=0; i=0
        name=""; id=""; courseName=""
        while k<len(stringLine):
            if stringLine[k]!=":":
                val=""
                for j in range(k,len(stringLine)):
                    if stringLine[j]!=":":
                        val+=stringLine[j]
                        k+=1
                    else:
                        break
                if i==0:
                    name=val
                    i+=1
                elif i==1:
                    id=val
                    i+=1
                elif i==2:
                    courseName=val
            else:
                k+=1
        students[name]=f"{id}:{courseName}"
    else:
        if "_" in stringLine:
            temp=[]
            for k in range(0,len(stringLine)):
                if stringLine[k]=="_":
                    temp.append(" ")
                else:
                    temp.append(stringLine[k])
            stringLine="".join(temp)

        for k in students:
            if stringLine in students[k]:
                id=""
                for j in range(0,len(students[k])):
                    if students[k][j]!=":":
                        id+=students[k][j]
                    else:
                        break
                print(f"{k} - {id}")
            else:
                continue
        break
