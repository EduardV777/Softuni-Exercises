class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        if self.ind == len(self.sequence):
            self.ind = 0

        val = self.sequence[self.ind]
        self.ind += 1
        self.number -= 1
        return val


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')