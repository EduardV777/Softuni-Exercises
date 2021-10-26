n=int(input())
sum=0
for k in range(1,n+1):
    char=input()
    code=ord(char)
    sum+=code
print(f"The sum equals: {sum}")
