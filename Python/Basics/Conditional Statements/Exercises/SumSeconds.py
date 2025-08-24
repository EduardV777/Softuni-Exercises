from math import floor

comp1 = int(input())        #seconds
comp2 = int(input())
comp3 = int(input())


sumTime = comp1 + comp2 + comp3

minutes = floor(sumTime / 60)
seconds = round((sumTime / 60 - floor(sumTime / 60)) * 60)



output = f"{minutes}:"

if 0 <= seconds < 10:
    output += f"0{seconds}"
else:
    output += f"{seconds}"

print(output)