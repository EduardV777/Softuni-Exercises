import re
txt=input()

findPairs=re.compile(r"(@|#){1}([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1")
occurrences=findPairs.findall(txt)

mirrorWords=[]
for k in range(0,len(occurrences)):
    firstWord=occurrences[k][1]; secondWord=occurrences[k][2]
    secondWordRev=[e for e in secondWord]
    secondWordRev.reverse()
    secondWordRev=''.join(secondWordRev)
    if firstWord==secondWordRev:
        mirrorWords.append([firstWord, secondWord])
output=""
for j in range(0,len(mirrorWords)):
    output+=mirrorWords[j][0]+" <=> "+mirrorWords[j][1]
    if j!=len(mirrorWords)-1:
        output+=", "
if len(occurrences)!=0:
    print(f"{len(occurrences)} word pairs found!")
else:
    print("No word pairs found!")

if len(mirrorWords)!=0:
    print(f"The mirror words are:")
    print(output)
else:
    print("No mirror words!")
