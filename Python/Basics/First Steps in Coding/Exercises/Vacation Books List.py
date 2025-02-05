pagesInBook = int(input())
pagesReadPerHour = int(input())
daysToRead = int(input())

hoursToSetDaily = (pagesInBook / pagesReadPerHour) / daysToRead

print(round(hoursToSetDaily))