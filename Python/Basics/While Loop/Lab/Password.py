user = input()
password = input()

while True:
    passAttempt = input()

    if passAttempt == password:
        print(f"Welcome {user}!")
        break