import re
text=""
while True:
    usrInput=input()
    if usrInput!="":
        text+=usrInput+"\n"
    else:
        break
lookForNumbers=re.compile(r"\d+")
nums=lookForNumbers.findall(text)
print(' '.join(nums))
