month = input()
nights = int(input())
totalApartment = 0
totalStudio = 0

prices = [ [50, 65], [75.20, 68.70], [76, 77]] # may/october - june/sept - jul/aug

# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

if month == "May" or month == "October":
    totalApartment = nights * prices[0][1]
    totalStudio = nights * prices[0][0]

    if 7 < nights <= 14:
        totalStudio -= totalStudio * 0.05
    elif nights > 14:
        totalStudio -= totalStudio * 0.30
        totalApartment -= totalApartment * 0.10

elif month == "June" or month == "September":
    totalApartment = nights * prices[1][1]
    totalStudio = nights * prices[1][0]

    if nights > 14:
        totalStudio -= totalStudio * 0.2
        totalApartment -= totalApartment * 0.10

elif month == "July" or month == "August":
    totalApartment = nights * prices[2][1]
    totalStudio = nights * prices[2][0]

    if nights > 14:
        totalApartment -= totalApartment * 0.10

print(f"Apartment: {totalApartment:.2f} lv.\nStudio: {totalStudio:.2f} lv.")