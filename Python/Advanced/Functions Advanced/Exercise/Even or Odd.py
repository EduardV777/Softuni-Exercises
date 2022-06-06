def even_odd(*args):
    command=args[-1]
    numbers=[e for e in args if type(e)!=str]
    if command=="even":
        numbers=[e for e in numbers if e%2==0]
    else:
        numbers=[e for e in numbers if e%2!=0]
    return numbers