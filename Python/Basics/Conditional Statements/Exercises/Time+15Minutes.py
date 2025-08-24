from math import floor
output = ""


hours = int(input())
minutes = int(input())

time = (hours * 60) + minutes
time += 15

newHours = floor(time / 60)
newMinutes = round((time / 60 - floor(time / 60)) * 60)

if newHours == 24:
    newHours = 0
    output = f"{newHours}:"
else:
    output += f"{newHours}:"

if 0 <= newMinutes < 10:
    output += f"0{newMinutes}"
else:
    output += f"{newMinutes}"

print(output)