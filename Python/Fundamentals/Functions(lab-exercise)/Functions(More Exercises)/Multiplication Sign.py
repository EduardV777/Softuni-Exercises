int1=int(input()); int2=int(input()); int3=int(input())
def MultiplyResult():
    signResult=""
    if int1==0 or int2==0 or int3==0:
        signResult="zero"
    elif (int1<0 and int2<0 and int3>0) or (int2<0 and int3<0 and int1>0) or (int1<0 and int3<0 and int2>0):
        signResult="positive"
    elif int1<0 or int2<0 or int3<0:
        signResult="negative"
    else:
        signResult="positive"
    return signResult
print(MultiplyResult())
