currentBookPages = int(input())
pagesPerHour = int(input())
daysLeft = int(input())

hoursPerDayNeeded = (currentBookPages / pagesPerHour) / daysLeft

print(round(hoursPerDayNeeded))