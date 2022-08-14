class vowels:
    
    def __init__(self, string: str):
        self.string = [char for char in string]
        self.vowels = ["a", "e", "y", "u", "o", "i"]
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.ind == len(self.string):
                raise StopIteration

            val = self.string[self.ind]
            self.ind += 1
            if val.lower() in self.vowels:
                return val
        
    # def genFunc(self):
    #     return (x for x in self.string if x.lower() in self.vowels)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

# mystring2 = vowels('Abcedifuty0o')
# print(next(mystring2.genFunc()))