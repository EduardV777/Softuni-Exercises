class MustContainAtSymbolError(Exception):
    def __init__(self, txt):
        errMsg=txt

class NameTooShortError(Exception):
    def __init__(self, txt):
        errMsg=txt

class InvalidDomainError(Exception):
    def __init__(self, txt):
        errMsg=txt


while True:
    email=input()
    if email!="End":
        if not "@" in email:
            raise MustContainAtSymbolError("Email must contain @")
        else:
            email=email.split("@")

        if not len(email[0])>4:
            raise NameTooShortError("Name must be more than 4 characters")

        if not '.bg' in email[1] and not '.net' in email[1] and not '.com' in email[1] and not '.org' in email[1]:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        print("Email is valid")
    else:
        break