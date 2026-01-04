integers = input().split(", ")

def palindromes(seq: list):

    seq = [int(k) for k in seq]

    for k in range(0, len(seq)):
        seq[k] = str(seq[k])

        forw = [str(i) for i in seq[k]]
        rev = [str(i) for i in seq[k][-1::-1]]

        if "".join(forw) == "".join(rev):
            print("True")
        else:
            print("False")

palindromes(integers)