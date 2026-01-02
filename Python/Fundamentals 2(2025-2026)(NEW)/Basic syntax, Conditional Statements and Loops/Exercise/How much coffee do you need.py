coffees = 0

while True:

    comm = input()

    if not comm == "END":
        add = 0

        if comm.isupper():
            comm = comm.lower()
            add = 2
        else:
            add = 1

        if comm == "coding" or comm == "dog" or comm == "cat" or comm == "movie":
            coffees += add
        else:
            continue

    else:
        break
if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")