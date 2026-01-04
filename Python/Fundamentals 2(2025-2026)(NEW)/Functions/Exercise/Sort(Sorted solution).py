sequence = input().split(" ")

def sortValues(seq: list):
    seq = [int(k) for k in seq]
    seq = sorted(seq)

    return seq

sequence = sortValues(sequence)

print(sequence)