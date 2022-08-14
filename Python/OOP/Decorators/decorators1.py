def uppercase(funcText):
    def wrapper():
        res = funcText()
        res = res.upper()
        return res

    return wrapper

def say_hi():
    return "say_hi"

decorator = uppercase(say_hi)
print(decorator())