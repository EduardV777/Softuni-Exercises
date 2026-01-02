string=input()
string=string.split()
alphabetLower=[]; alphabetUpper=[]
letters1=65; letters2=97

for k in range(0,26):
    alphabetLower.append(chr(letters2))
    alphabetUpper.append(chr(letters1))
    letters1+=1; letters2+=1

totalSum=0
for k in range(0,len(string)):
    letters=[]; number=""
    for j in range(0,len(string[k])):
        if string[k][j].isdigit():
            number+=string[k][j]
        elif string[k][j].isalpha():
            letters.append(string[k][j])
    number=int(number)
    #letter 1 process
    if letters[0].isupper():
        letterPos1=alphabetUpper.index(letters[0])+1
        res=number/letterPos1
    else:
        letterPos1=alphabetLower.index(letters[0])+1
        res=number*letterPos1
    #letter 2 process
    if letters[1].isupper():
        letterPos2=alphabetUpper.index(letters[1])+1
        res-=letterPos2
    else:
        letterPos2=alphabetLower.index(letters[1])+1
        res+=letterPos2
    totalSum+=res
print(f"{totalSum:.2f}")
