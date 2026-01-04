def filterEvens():
    seq = input().split(" ")
    seq = [int(k) for k in seq]

    seq = [k for k in seq if k % 2 == 0]

    print(seq)

filterEvens()