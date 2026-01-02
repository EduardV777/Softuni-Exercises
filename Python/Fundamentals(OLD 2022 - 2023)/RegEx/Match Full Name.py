import re
fullName=re.compile(r"\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b")
names=input()
listMatches=fullName.findall(names)
print(f"{' '.join(listMatches)}")
