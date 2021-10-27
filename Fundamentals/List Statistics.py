n=int(input())
positives=[]; negatives=[]
for k in range(1,n+1):
    num=int(input())
    if num<0:
        negatives.append(num)
    else:
        positives.append(num)
sumNegatives=0
for k in range(0,len(negatives)):
    sumNegatives+=negatives[k]
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}\nSum of negatives: {sumNegatives}")
