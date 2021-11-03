int1=int(input()); int2=int(input())
def FactorialDiv(num1,num2):
    fact1=1; fact2=1
    for k in range(1,num1+1):
        fact1*=k
    for j in range(1,num2+1):
        fact2*=j
    res=fact1/fact2
    return f"{res:.2f}"
print(FactorialDiv(int1,int2))
