accounts = ["EduardV", "John3", "Maria19"]

accountsIterator = iter(accounts)

while True:
    try:
        print(next(accountsIterator))
    except StopIteration:
        break

print("\nFinished!")