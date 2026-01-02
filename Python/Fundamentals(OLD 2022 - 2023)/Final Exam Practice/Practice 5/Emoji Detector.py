import re
usrEntry=input()
findEmojis=re.compile(r"\B([:|*]{2})([A-Z]{1,}[a-z]{2,})\1\B")
findDigits=re.compile(r"[1-9]+")
emojisFound=[]
occurrences=findEmojis.findall(usrEntry)
digitsFound=findDigits.findall(usrEntry)
coolThreshold=''.join(digitsFound)
coolThreshold=[int(e) for e in coolThreshold]

for k in range(0,len(occurrences)):
    reaction=occurrences[k][1]
    coolness=0
    for j in range(0,len(reaction)):
        coolness+=ord(reaction[j])
    emojisFound.append([reaction, coolness, occurrences[k][0]])
cool=0
for k in range(0,len(coolThreshold)):
    if k==0:
        cool=1
    cool*=coolThreshold[k]
coolThreshold=cool
print(f"Cool threshold: {coolThreshold}")
print(f"{len(emojisFound)} emojis found in the text. The cool ones are:")
for j in range(0,len(emojisFound)):
    if emojisFound[j][1]>coolThreshold:
        print(f"{emojisFound[j][2]}{emojisFound[j][0]}{emojisFound[j][2]}")
