def solution():
    def integers():
        numInt = 1
        while True:
            val = numInt
            numInt += 1
            yield val
        #inifinite amount of integers

    def halves():
        val = 0
        for i in integers():
            val = i / 2
            yield val

    

    def take(n, seq):
        list = []
        val = 0

        while n > 0:
            val = next(seq)
            n -= 1
            list.append(val)
            
        return list

    return (take, halves, integers)

#solution()

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))