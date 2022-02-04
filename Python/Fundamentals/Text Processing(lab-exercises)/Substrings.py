str1=input(); str2=input()
while str1 in str2:
    str2=str2.replace(str1,"")
print(str2)
