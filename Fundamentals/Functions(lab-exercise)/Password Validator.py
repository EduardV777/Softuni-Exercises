password=input()
def CheckPassword(passw):
    digits=0; msg=""; valid=True
    if not 6 <= len(passw) <= 10:
        msg+="Password must be between 6 and 10 characters\n"
        valid=False
    for j in range(0,len(passw)):
        if not 97<=ord(passw[j])<=122 and not 65<=ord(passw[j])<=90 and not 48<=ord(passw[j])<=57:
            msg+="Password must consist only of letters and digits\n"
            valid=False
            break
        else:
            if passw[j].isdigit():
                digits+=1
    if digits<2:
        msg+="Password must have at least 2 digits"
        valid=False
    if valid==True:
        return "Password is valid"
    else:
        return msg
print(CheckPassword(password))
