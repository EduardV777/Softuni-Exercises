book = input()
c = 0
while True:
    bookTest = input()

    if bookTest == book:
        print(f"You checked {c} books and found it.")
        break

    elif bookTest == "No More Books":
        print(f"The book you search is not here!\nYou checked {c} books.")
        break

    else:
        c+= 1