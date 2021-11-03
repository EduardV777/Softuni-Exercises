num=int(input())
def LoadingBar(value=0):
    barLength=value//10; bar=""
    for k in range(1,11):
        if k<=barLength:
            bar+="%"
        else:
            bar+="."
    if barLength<10:
        return f"{barLength*10}% [{bar}]\nStill loading..."
    else:
        return f"{barLength*10}% Complete!\n[{bar}]"
print(LoadingBar(num))
