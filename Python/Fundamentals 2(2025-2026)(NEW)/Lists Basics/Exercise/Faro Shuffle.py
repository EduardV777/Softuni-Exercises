#Note about task - the length of the deck will always be an even number

deck = input().split(" ")
shuffles = int(input())

for k in range(1, shuffles + 1):

    deck1 = []
    deck2 = []

    for k in range(0, len(deck)):
        if k < len(deck) / 2:
            deck1.append(deck[k])
        else:
            deck2.append(deck[k])

    turn = True
    c = 0

    for k in range(0, len(deck)):
        if turn:
            deck[k] = deck1[c]
            turn = False
        else:
            deck[k] = deck2[c]
            turn = True
            c += 1

print(deck)