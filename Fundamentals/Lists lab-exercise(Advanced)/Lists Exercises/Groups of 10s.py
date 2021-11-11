numbers=input()
numbersL=[]
k=0
while k<len(numbers):
    num=""
    if numbers[k]!=" ":
        for j in range(k,len(numbers)):
            if numbers[j]!=",":
                num+=numbers[j]
                k+=1
            else:
                k+=1
                break
        num=int(num)
        numbersL.append(num)
    else:
        k+=1
maxVal=max(numbersL); output=""
groups10s=list(filter(lambda x: 1<=x<=10,numbersL))
output+=f"Group of 10's: {groups10s}\n"
if maxVal>10:
    groups20s=list(filter(lambda x: 11<=x<=20,numbersL))
    output+=f"Group of 20's: {groups20s}\n"
if maxVal>20:
    groups30s=list(filter(lambda x: 21<=x<=30,numbersL))
    output+=f"Group of 30's: {groups30s}\n"
if maxVal>30:
    groups40s=list(filter(lambda x: 31<=x<=40,numbersL))
    output+=f"Group of 40's: {groups40s}\n"
if maxVal>40:
    groups50s=list(filter(lambda x: 41<=x<=50,numbersL))
    output+=f"Group of 50's: {groups50s}"
print(output)
