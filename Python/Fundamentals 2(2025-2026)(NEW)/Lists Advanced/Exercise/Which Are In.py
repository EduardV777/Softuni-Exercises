txt1 = input().split(", ")
txt2 = input().split(", ")

def checkSequenceItems(x, seq: list):
    for k in range(0, len(seq)):
        if x in seq[k]:
            return True

    return False

def makeNewList(seq1: list, seq2: list):
    new = list(filter(lambda x: checkSequenceItems(x, seq2), seq1))
    return new

txt3 = makeNewList(txt1, txt2)

print(txt3)