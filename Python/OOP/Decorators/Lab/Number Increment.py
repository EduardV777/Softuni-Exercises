def number_increment(numbers):

    def increase():
        res = [e + 1 for e in numbers]
        return res

    return increase()


print(number_increment([1, 2, 3]))