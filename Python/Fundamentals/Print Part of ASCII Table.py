n1=int(input()); n2=int(input())
chars=[]
for k in range(n1,n2+1):
    char=chr(k)
    chars.append(char)
print(" ".join(chars))
