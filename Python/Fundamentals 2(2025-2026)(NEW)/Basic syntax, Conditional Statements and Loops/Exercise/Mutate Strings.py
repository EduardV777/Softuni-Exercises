txt1 = input()
txt2 = input()

transform = ""
log = ""

if len(txt1) == len(txt2):

    for k in range(0,len(txt2)):
        orig = ""
        transform += txt2[k]

        for c in range(k + 1, len(txt1)):
            orig += txt1[c]

        if (transform + orig) != log:
            print(f"{transform}" + orig)
            log = transform + orig
