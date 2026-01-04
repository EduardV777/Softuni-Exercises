def absVals():
    seq = input().split(" ")

    seq = [abs(float(k)) for k in seq if type(k) == str]

    print(seq)

absVals()