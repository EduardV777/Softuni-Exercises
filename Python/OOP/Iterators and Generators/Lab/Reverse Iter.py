class reverse_iter:

    def __init__(self, iterable):
        self.iterable = [x for x in iterable]
        self.index = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == -1:
            raise StopIteration
            
        val = self.iterable[self.index]
        self.index -= 1
        return val


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

print("\n")

reversed_list = reverse_iter((4, 3, 2, 1))
for item in reversed_list:
    print(item)