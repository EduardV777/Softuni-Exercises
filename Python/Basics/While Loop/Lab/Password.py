name = input()
password = input()

while True:
    passConfirm = input()

    if password == passConfirm:
        print(f"Welcome {name}!")
        break