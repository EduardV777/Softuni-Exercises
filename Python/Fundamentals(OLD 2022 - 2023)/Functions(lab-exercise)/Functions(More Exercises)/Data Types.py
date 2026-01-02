strType=input()
def ProcessStr(stringType):
    str=input()
    if stringType=="int":
        str=int(str)
        str*=2
    elif stringType=="real":
        str=float(str); str*=1.5
        str=f"{str:.2f}"
    elif stringType=="string":
        symbols=["$"]
        for k in range(0,len(str)):
            symbols.append(str[k])
        symbols.append("$")
        str="".join(symbols)
    return str
print(ProcessStr(strType))
