sequence = input().split(" ")

def minMaxSum(seq: list):

    seq = [int(k) for k in seq]

    minimum = min(seq)
    maximum = max(seq)
    sumRes = sum(seq)

    print(f"The minimum number is {minimum}\nThe maximum number is {maximum}\nThe sum number is: {sumRes}")

minMaxSum(sequence)