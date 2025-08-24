from math import floor

examHour = int(input())
examMinute = int(input())
arrivalHour = int(input())
arrivalMinute = int(input())
output = ""
arrival = ""

examTime = (examHour * 60) + examMinute
arrivalTime = (arrivalHour * 60) + arrivalMinute

difference = arrivalTime - examTime

if arrivalTime <= examTime:
    difference = abs(difference)

    if difference <= 30:
        arrival = "On time"
    else:
        arrival = "Early"

else:
    arrival = "Late"


if arrival == "On time" or arrival == "Early":
    if 0 < difference < 60 :
        print(f"{arrival}\n{difference} minutes before the start")
    elif difference == 0:
        print(f"{arrival}")
    elif difference >= 60:
        arrivalHourDiff = floor(difference / 60)
        arrivalMinuteDiff = round(((difference / 60) - (floor(difference / 60))) * 60)

        output = f"{arrivalHourDiff}:"
        if arrivalMinuteDiff < 10:
            output += f"0{arrivalMinuteDiff} "
        else:
            output += f"{arrivalMinuteDiff} "

        output += "hours before the start"

        print(f"{arrival}\n{output}")

elif arrival == "Late":
    if 0 < difference < 60:
        print(f"{arrival}\n{difference} minutes after the start")
    elif difference >= 60:
        arrivalHourDiff = floor(difference / 60)
        arrivalMinuteDiff = round(((difference / 60) - (floor(difference / 60))) * 60)

        output = f"{arrivalHourDiff}:"
        if arrivalMinuteDiff < 10:
            output += f"0{arrivalMinuteDiff} "
        else:
            output += f"{arrivalMinuteDiff} "

        output += " hours after the start"

        print(f"{arrival}\n{output}")