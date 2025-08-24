currentPagesLeft = int(input()) #345 212
pagesReadPerHour = int(input()) # 50 20
daysLeft = int(input()) # 20 2

allocateHoursPerDay = (currentPagesLeft / pagesReadPerHour) / daysLeft

print(round(allocateHoursPerDay))