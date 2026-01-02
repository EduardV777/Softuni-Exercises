seq=input()
k=0; words={}
while k<len(seq):
    if seq[k]!=" ":
        found=False
        val=""
        for j in range(k,len(seq)):
            if seq[j]!=" ":
                val+=seq[j]
                k+=1
            else:
                break
        for i in words:
            if i==val.lower():
                words[i]+=1; found=True
                break
        if found==False:
            words[val.lower()]=0
    else:
        k+=1
output=""
for k in words:
    if words[k]%2==0:
        output+=k+" "
print(output)
