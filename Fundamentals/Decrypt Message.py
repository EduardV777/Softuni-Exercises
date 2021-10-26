key=int(input()); n=int(input())
decryptedMsg=[]
for k in range(1,n+1):
    letter=input()
    decLetter=ord(letter)+key
    decLetter=chr(decLetter)
    decryptedMsg.append(decLetter)
print("".join(decryptedMsg))
