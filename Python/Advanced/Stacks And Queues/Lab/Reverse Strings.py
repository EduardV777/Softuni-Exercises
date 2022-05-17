string=input()

newString=""

def reverseWordsInString(txt):
    stackStr=[]; newString=""
    for k in range(0,len(txt)):
        stackStr.append(txt[k])

    while stackStr:
        newString+=stackStr[-1]
        stackStr.pop()
    return newString

newString=reverseWordsInString(string)

print(newString)