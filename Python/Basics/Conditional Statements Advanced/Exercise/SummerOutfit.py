deg = int(input())
dayPart = input()
outfit = ""
shoes = ""
suggestions = [ [["Sweatshirt", "Sneakers"],["Shirt", "Moccasins"],["T-Shirt", "Sandals"]], [["Shirt", "Moccasins"],["T-Shirt", "Sandals"],["Swim Suit", "Barefoot"]], [["Shirt", "Moccasins"],["Shirt", "Moccasins"],["Shirt", "Moccasins"]] ] #morning afternoon evening


if 10 <= deg <= 18:
    if dayPart == "Morning":
        outfit = suggestions[0][0][0]
        shoes = suggestions[0][0][1]
    elif dayPart == "Afternoon":
        outfit = suggestions[1][0][0]
        shoes = suggestions[1][0][1]
    elif dayPart == "Evening":
        outfit = suggestions[2][0][0]
        shoes = suggestions[2][0][1]

elif 18 < deg <= 24:
    if dayPart == "Morning":
        outfit = suggestions[0][1][0]
        shoes = suggestions[0][1][1]
    elif dayPart == "Afternoon":
        outfit = suggestions[1][1][0]
        shoes = suggestions[1][1][1]
    elif dayPart == "Evening":
        outfit = suggestions[2][1][0]
        shoes = suggestions[2][1][1]

elif deg >= 25:
    if dayPart == "Morning":
        outfit = suggestions[0][2][0]
        shoes = suggestions[0][2][1]
    elif dayPart == "Afternoon":
        outfit = suggestions[1][2][0]
        shoes = suggestions[1][2][1]
    elif dayPart == "Evening":
        outfit = suggestions[2][2][0]
        shoes = suggestions[2][2][1]

print(f"It's {deg} degrees, get your {outfit} and {shoes}.")