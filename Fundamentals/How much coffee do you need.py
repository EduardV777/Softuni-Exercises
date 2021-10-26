event=""; coffees=0
while event!="END":
    event=input()
    if event!="END":
        if event.isupper():
            if event!="CODING" and event!="DOG" and event!="CAT" and event!="MOVIE":
                continue
            else:
                coffees+=2
        else:
            if event!="coding" and event!="dog" and event!="cat" and event!="movie":
                continue
            else:
                coffees+=1
if coffees>5:
    print("You need extra sleep")
else:
    print(coffees)
