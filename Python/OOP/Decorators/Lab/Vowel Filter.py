def vowel_filter(function):

    def wrapper():
        vowels = ["a","i","o","u","e","y"]
        res = function()
        res = [e for e in res if e.lower() in vowels]
        return res

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
