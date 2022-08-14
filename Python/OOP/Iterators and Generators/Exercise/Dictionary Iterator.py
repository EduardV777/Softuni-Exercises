class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.ind = 0
    def __iter__(self):
        return self

    def __next__(self):
        dictKeys = list(self.dictionary.keys())

        if self.ind == len(dictKeys):
            raise StopIteration

        val = (dictKeys[self.ind], self.dictionary[dictKeys[self.ind]])
        self.ind += 1
        return val
            


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)