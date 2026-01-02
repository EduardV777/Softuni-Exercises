#Happy year is the year with only distinct digits

currentYear = int(input())

while True:
    happy = True
    currentYear += 1
    year = str(currentYear)

    for k in range(0, len(year)):
        digit = year[k]
        times = year.count(digit)

        if times > 1:
            happy = False
            break

    if happy:
        print(currentYear)
        break