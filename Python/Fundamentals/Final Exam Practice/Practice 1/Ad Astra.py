import re
singleStr=input()
totalCal=0; survivalDays=0
findFoodData=re.compile(r"(?P<FirstSymb>[|\|#])([A-Za-z\s]+)(?P=FirstSymb)([0-9]{2}/[0-9]{2}/[0-9]{2})(?P=FirstSymb)([0-9]{1,5})(?P=FirstSymb)")
found=findFoodData.findall(singleStr)
for k in range(0,len(found)):
    totalCal+=int(found[k][3])
survivalDays=totalCal//2000
print(f"You have food to last you for: {survivalDays} days!")
for k in range(0,len(found)):
    print(f"Item: {found[k][1]}, Best before: {found[k][2]}, Nutrition: {found[k][3]}")
