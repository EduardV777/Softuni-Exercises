txt=input()
txtSymbols=[]
for j in range(0,len(txt)):
    txtSymbols.append(txt[j])
k=0
while k<len(txtSymbols):
    if txtSymbols[k]=="a" or txtSymbols[k]=="o" or txtSymbols[k]=="u" or txtSymbols[k]=="e" or txtSymbols[k]=="i" or\
       txtSymbols[k]=="A" or txtSymbols[k]=="O" or txtSymbols[k]=="U" or txtSymbols[k]=="E" or txtSymbols[k]=="I":
        del txtSymbols[k]
        continue
    else:
        k+=1
print("".join(txtSymbols))
