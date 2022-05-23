txt=input()

txtTup=tuple(e for e in txt)

characters={}

for k in txtTup:
    characters[k]=txtTup.count(k)

for k in sorted(characters):
    print(f"{k}: {characters[k]} time/s")
