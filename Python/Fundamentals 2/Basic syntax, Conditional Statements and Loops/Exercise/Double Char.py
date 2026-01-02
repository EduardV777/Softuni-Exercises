while True:

    txt = input()

    if not txt == "End":

        if txt == "SoftUni":
            continue

        newTxt = ""

        for k in range(0, len(txt)):
            newTxt += txt[k] * 2

        print(newTxt)

    else:
        break