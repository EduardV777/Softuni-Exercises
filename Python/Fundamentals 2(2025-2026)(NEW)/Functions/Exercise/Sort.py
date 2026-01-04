sequence = input().split(" ")

def sortSequence(s: list):
    s = [int(k) for k in s]

    for k in range(0, len(s)): # 7
        currVal = s[k]
        pos = k

        for j in range(k + 1, len(s)):
            if currVal > s[j]:
                a = s[j]
                s[j] = currVal
                s[pos] = a
                pos = j

            currVal = s[k]
            pos = k

            for q in range(len(s) - k, 0):
                if currVal > s[q]:
                    a = s[q]
                    s[q] = currVal
                    s[pos] = a
                    pos = q

    return s

sequence = sortSequence(sequence)

print(sequence)


# 12 52 53 11 2 8 45