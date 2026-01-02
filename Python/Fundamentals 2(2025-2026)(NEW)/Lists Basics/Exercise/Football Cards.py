a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = list(a)

cards = input()

cards = cards.split(" ")

terminated = False

for k in range(0, len(cards)):
    card = cards[k].split("-")
    card[1] = int(card[1])

    if card[0] == "A":
        if card[1] in a:
            if a.count(card[1]) != 0:
                a.remove(card[1])

    elif card[0] == "B":
        if card[1] in b:
            if b.count(card[1]) != 0:
                b.remove(card[1])

    if len(a) < 7 or len(b) < 7:
        terminated = True
        break

print(f"Team A - {len(a)}; Team B - {len(b)}")

if terminated:
    print("Game was terminated")
