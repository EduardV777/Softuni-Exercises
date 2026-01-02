import re
someStr=input()
extractEmails=re.compile(r"\b([A-Za-z]+[-|.|,|_]*[A-Za-z]+)([@]{1})([A-Za-z]+[-]?[A-Za-z]+[.]{1}[A-Za-z]+)([.]{1}[A-Za-z]+[-]?[A-Za-z]+){0,}\b")
emails=extractEmails.finditer(someStr)
for email in emails:
    print(email.group(0))
