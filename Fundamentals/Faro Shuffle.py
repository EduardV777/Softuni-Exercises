deck=input(); shuffles=int(input())
deck=deck.split(" ")
deck1=[]; deck2=[]
halfDeck=int(len(deck)/2)

for j in range(shuffles,0,-1):
    deck1=deck[0:halfDeck]
    deck2=deck[halfDeck:]
    deck = []
    for k in range(0,len(deck1)):
        deck.append(deck1[k])
        deck.append(deck2[k])
print(deck)
