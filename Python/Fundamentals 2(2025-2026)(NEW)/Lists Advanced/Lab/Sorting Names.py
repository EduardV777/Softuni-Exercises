names = input().split(", ")

def sortByLength(seq: list, order = False):
    #False order - descending by default

    if not order:
        seq = sorted(seq, key = lambda x: -len(x))
    else:
        pass

    #Look for names with same length and sort alphabetically in ascending order if such names are present(separately)
    x = []
    ind = 0
    end = 0

    for k in range(0, len(seq) - 1):
        #such names are present
        if len(seq[k]) == len(seq[k + 1]):
          ind = k
          x.append(seq[k])
          x.append(seq[k + 1])

          #check for additional names with the same length and separate for asc alphabetical sorting
          #starting and ending positions of same length names should be noted
          for j in range(k + 1, len(seq)):
            if not j == len(seq) - 1 and len(seq[j]) == len(seq[j + 1]):
                x.append(seq[j])
                x.append(seq[j + 1])
            else:
                end = j
                break

          x.sort()

          #bring the names back into the original list by positions
          for c in range(ind, end + 1):
              seq[c] = x[0]
              x.pop(0)


    return seq

names = sortByLength(names)

print(names)

