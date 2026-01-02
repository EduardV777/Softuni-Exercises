while True:

    name = input()

    if not name == "Welcome!":

        if not name == "Voldemort":

            if len(name) < 5:
                print(f"{name} goes to Gryffindor.")
            elif len(name) == 5:
                print(f"{name} goes to Slytherin.")
            elif len(name) == 6:
                print(f"{name} goes to Ravenclaw.")
            else:
                print(f"{name} goes to Hufflepuff.")

        else:
            print("You must not speak of that name!")
            break

    else:
        print("Welcome to Hogwarts.")
        break