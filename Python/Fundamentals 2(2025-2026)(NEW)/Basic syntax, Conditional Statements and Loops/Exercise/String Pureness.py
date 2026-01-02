n = int(input())

while n:
    txt = input()

    if not ("," in txt or "." in txt or "_" in txt):
        print(f"{txt} is pure.")
    else:
        print(f"{txt} is not pure!")

    n -= 1