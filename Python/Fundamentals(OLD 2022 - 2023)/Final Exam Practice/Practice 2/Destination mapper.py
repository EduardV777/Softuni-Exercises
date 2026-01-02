import re
places=input()
findPlaces=re.compile(r"(?P<FirstSymb>[=|/]){1}([A-Z][A-Za-z]{2,})(?P=FirstSymb){1}")
placesList=findPlaces.findall(places)
destinations=[]; travelPoints=0
for k in range(0,len(placesList)):
    destinations.append(placesList[k][1])
    travelPoints+=len(placesList[k][1])
print(f"Destinations: {', '.join(destinations)}\nTravel Points: {travelPoints}")
