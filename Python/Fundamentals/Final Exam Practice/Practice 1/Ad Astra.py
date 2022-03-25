import re
text=input()
validFoodInfo=re.compile(r"[#|\|]{1}(?P<itemName>[A-Za-z\s]+)[#|\|]{1}(?P<expiry>[0-9]{2}/[0-9]{2}/[0-9]{2})[#|\|]{1}(?P<calories>[0-9]+)[#|\|]{1}")
totalCals=0
foodData=validFoodInfo.findall(text)
outputFoodData=""
for k in range(0,len(foodData)):
    totalCals+=int(foodData[k][2])
    outputFoodData+=f"Item: {foodData[k][0]}, Best before: {foodData[k][1]}, Nutrition: {foodData[k][2]}"
    if k!=len(foodData)-1:
        outputFoodData+="\n"
print(f"You have food to last you for: {totalCals//2000} days!")
print(outputFoodData)
