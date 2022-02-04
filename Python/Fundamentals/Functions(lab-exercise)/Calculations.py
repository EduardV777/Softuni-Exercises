op=input(); a1=int(input()); a2=int(input())
def calc(operator="", x1=1, x2=1):
    if operator=="substract":
        res=x1-x2
    elif operator=="divide":
        res=x1//x2
    elif operator=="add":
        res=x1+x2
    elif operator=="multiply":
        res=x1*x2
        #hotfix
    else:
        res=x1-x2
    return res
print(calc(op,a1,a2))
