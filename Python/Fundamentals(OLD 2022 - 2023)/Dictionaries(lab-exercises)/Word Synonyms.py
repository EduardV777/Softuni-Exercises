n=int(input())
synonymsDict={}
for k in range(0,n):
    wordFound=False
    word=input(); synon=input()
    for j in synonymsDict:
        if j==word:
            synonymsDict[j]+=f", {synon}"
            wordFound=True
    if wordFound==False:
        synonymsDict[word]=synon
output=""
for k in synonymsDict:
    output+=f"{k} - {synonymsDict[k]}\n"
print(output)
