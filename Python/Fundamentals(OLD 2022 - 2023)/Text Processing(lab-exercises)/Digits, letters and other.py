str1=input()
digits=""; letters=""; others=""
for k in range(0,len(str1)):
    if str1[k].isdigit():
        digits+=str1[k]
    elif str1[k].isalpha():
        letters+=str1[k]
    else:
        others+=str1[k]
print(digits)
print(letters)
print(others)
