def fibonacci():
    prev = -1
    next = 1
    startSeq = True

    while True:
        if prev == -1:
            prev += 1
            yield 0
            yield 1
            continue
        
        next = next + prev
        prev = next - prev
        yield next
        


generator = fibonacci()
for i in range(5):
    print(next(generator))