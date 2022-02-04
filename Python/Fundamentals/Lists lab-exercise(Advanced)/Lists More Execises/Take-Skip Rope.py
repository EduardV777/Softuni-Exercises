txt=input()
numbers=[]; chars=[]; take=[]; skip=[]
res=[]
for k in range(0,len(txt)):
    if txt[k].isdigit()==True:
        numbers.append(int(txt[k]))
    else:
        chars.append(txt[k])
for j in range(0,len(numbers)):
    if j%2==0:
        take.append(numbers[j])
    else:
        skip.append(numbers[j])
m=0; lastStop=m
for i in range(0,len(take)):
    if not i>=len(take) or not i>=len(skip) or not m>=len(chars):
        while m<lastStop+(take[i]):
            if m>=len(chars):
                break
            if chars[m].isdigit()==True:
                res.append(chars[m])
            else:
                res.append(chars[m])
            m+=1
        n=skip[i]
        m+=n
        lastStop=m
    else:
        break
print("".join(res))
