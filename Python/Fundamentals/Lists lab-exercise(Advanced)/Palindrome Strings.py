words=input(); palindromeWord=input()
wordsList=[]; palindromes=[]
k=0; palindromeTimes=0
while k<len(words):
    word=""
    if words[k]!=" ":
        for j in range(k,len(words)):
            if words[j]!=" ":
                word+=words[j]
                k+=1
            else:
                k+=1
                break
        wordsList.append(word)
    else:
        k+=1
for j in range(0,len(wordsList)):
    reversedWord=""
    for k in range(len(wordsList[j])-1,-1,-1):
        reversedWord+=wordsList[j][k]
        #print(reversedWord)
    if wordsList[j]==reversedWord:
        palindromes.append(wordsList[j])
    if wordsList[j]==palindromeWord:
        palindromeTimes+=1
print(palindromes); print(f"Found palindrome {palindromeTimes} times")
