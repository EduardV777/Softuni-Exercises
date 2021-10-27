n=int(input())
word=input()
list=[]; filtered=[]
for k in range(1,n+1):
    str=input()
    list.append(str)
print(list)
for k in range(0,len(list)):
    if list[k].find(word)>-1:
        filtered.append(list[k])
print(filtered)
