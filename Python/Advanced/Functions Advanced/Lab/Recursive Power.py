def recursive_power(num,pow, currVal=1):
    currVal=currVal*num
    if pow!=1:
        return recursive_power(num,pow-1, currVal)
    else:
        return currVal