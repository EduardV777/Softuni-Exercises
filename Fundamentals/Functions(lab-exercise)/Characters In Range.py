c1=input(); c2=input()
def FindCharsBetween(char1,char2):
    n1=ord(char1)+1; n2=ord(char2)
    output=""
    for j in range(n1,n2):
        output+=str(chr(j))+" "
    return output
print(FindCharsBetween(c1,c2))
