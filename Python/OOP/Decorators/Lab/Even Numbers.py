def even_numbers(function):

    def wrapper(numbers):
        res = numbers
        res = [e for e in res if e % 2 == 0]
        return res

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
