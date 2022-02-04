import re
phoneNumbers=input()
pattern=re.compile(r"^[ ]*\+359[ |-]2[ |-][0-9]{3}[ |-][0-9]{4}")
matches=pattern.findall(phoneNumbers)
print(",".join(matches))
