budget = float(input())
season = input() #summer / winter

destination = ""
place = ""
spentMoney = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "winter":
        spentMoney = budget * 0.7
        place = "Hotel"
    elif season == "summer":
        spentMoney = budget * 0.3
        place = "Camp"

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "winter":
        spentMoney = budget * 0.8
        place = "Hotel"
    elif season == "summer":
        spentMoney = budget * 0.4
        place = "Camp"
else:
    destination = "Europe"
    spentMoney = budget * 0.9
    place = "Hotel"

print(f"Somewhere in {destination}\n{place} - {spentMoney:.2f}")
