seq = input().split(" ")
seq = [int(k) for k in seq]

def check(n):

    if n % 2 == 0:
        return True
    else:
        return False


seq = list(filter(check, seq))

print(seq)