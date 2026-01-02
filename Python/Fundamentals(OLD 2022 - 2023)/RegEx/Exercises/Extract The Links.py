import re
output=""
txt=input()
lookForLinks=re.compile(r"(www[.]{1}[-A-Za-z0-9]+)([.]{1}[a-z]+){1,}")
validLinks=lookForLinks.findall(txt)
for k in range(0,len(validLinks)):
    for j in range(0,len(validLinks[k])):
        output+=validLinks[k][j]
    if k!=len(validLinks)-1:
        output+="\n"
print(output)
