def operate(op, *args):
    res=""
    for k in range(0,len(args)):
        res+=str(args[k])
        if k!=len(args)-1:
            res+=op
    return eval(res)