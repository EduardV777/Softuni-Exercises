import re
text=input()
lookForVars=re.compile(r"\b([_])([A-Za-z]+)\b")
varNames=lookForVars.findall(text)
output=""
for k in range(0,len(varNames)):
    output+=varNames[k][1]
    if not k==len(varNames)-1:
        output+=","
print(output)
