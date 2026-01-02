symb1=input(); symb2=input(); string=input()
sumASCII=0
for k in range(0,len(string)):
    if ord(symb1)<ord(string[k])<ord(symb2):
        sumASCII+=ord(string[k])
print(sumASCII)
