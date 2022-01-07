import re
fullName=input()
fullName=fullName.split(", ")
validNames=""
pattern=re.compile(r"^[A-Z][a-z]+ [A-Z][a-z]+$")
for k in range(0,len(fullName)):
    if pattern.search(fullName[k]):
        validNames+=f"{fullName[k]} "
print(validNames)
