n1=input()
def OddEvenSum(n1):
    listNum=[]
    for j in range(0,len(n1)):
        listNum.append(int(n1[j]))
    oddSum=0; evenSum=0
    for k in range(0,len(listNum)):
        if listNum[k]%2==0:
            evenSum+=listNum[k]
        else:
            oddSum+=listNum[k]
    print(f"Odd sum = {oddSum}, Even sum = {evenSum}")
OddEvenSum(n1)
