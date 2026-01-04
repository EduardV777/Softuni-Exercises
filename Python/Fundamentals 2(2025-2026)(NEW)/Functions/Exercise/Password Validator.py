password = input()

def checkPassword(passw: str):

    valid = True
    twoDigitsReq = 0
    output = ""

    if not 6 <= len(passw) <= 10:
        output += "Password must be between 6 and 10 characters\n"
        valid = False

    passw = [k for k in passw]

    for char in passw:
        if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57):
            output += "Password must consist only of letters and digits\n"
            valid = False
            break
        elif 48 <= ord(char) <= 57:
            twoDigitsReq += 1

    if twoDigitsReq < 2:
        output += "Password must have at least 2 digits"
        valid = False

    return valid, output

validity = checkPassword(password)

if not validity[0]:
    print(validity[1])
else:
    print("Password is valid")