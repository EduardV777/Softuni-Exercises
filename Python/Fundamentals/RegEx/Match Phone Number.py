import re
validPhone=re.compile(r"(\+359\s2\s[0-9]{3}\s[0-9]{4}\b)|(\+359-2-[0-9]{3}-[0-9]{4}\b)")
phoneNumbers=input()
res=validPhone.findall(phoneNumbers)
for k in range(0,len(res)):
    for j in range(0,len(res[k])):
        if res[k][j]!="":
            res[k]=res[k][j]
            break
print(', '.join(res))
