from functools import wraps

def uppercase(funcText):
    @wraps(funcText)
    def wrapper():
        res = funcText()
        res = res.upper()
        return res

    return wrapper

@uppercase
def say_hi():
    return "say_hi"

print(say_hi())
print("\n")
print(say_hi.__name__)
print(say_hi.__doc__)