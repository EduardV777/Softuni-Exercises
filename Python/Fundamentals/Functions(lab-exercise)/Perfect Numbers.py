number=int(input())
def IsItPerfect(integer):
    perfect=True; divisors=[]; sum=0
    for j in range(1,integer):
        if integer%j==0:
            divisors.append(j)
    for k in range(0,len(divisors)):
        sum+=divisors[k]
    if sum!=integer:
        perfect=False
    if perfect==True:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."
print(IsItPerfect(number))
