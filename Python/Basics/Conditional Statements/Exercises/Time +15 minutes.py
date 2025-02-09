from math import floor

hours = int(input())
minutes = int(input())

shiftTime = (hours * 60 + minutes + 15)

hours = floor(shiftTime / 60)
minutes = shiftTime - (hours * 60)

if hours == 24:
    hours = 0

out = f"{hours}:"

if minutes < 10:
    out += f"0{minutes}"
else:
    out += f"{minutes}"

print(out)