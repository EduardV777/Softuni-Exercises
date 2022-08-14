items = ["item1", "second item", "third item"]

itemsIter = iter(items)

print(itemsIter)

print(next(itemsIter))
print(next(itemsIter))
print(itemsIter.__next__())
#print(itemsIter.__next__())