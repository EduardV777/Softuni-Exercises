numbers = input().split(", ")
numbers = list(map(int, numbers))

positive = list(filter(lambda n: n >= 0, numbers))
negative = list(filter(lambda n: n < 0, numbers))
even = list(filter(lambda n: n % 2 == 0, numbers))
odd = list(filter(lambda n: n % 2 != 0, numbers))

def backToStr(seq: list):
    seq = map(str, seq)

    return seq


print(f"Positive: {', '.join(backToStr(positive))}\nNegative: {', '.join(backToStr(negative))}\nEven: {', '.join(backToStr(even))}\nOdd: {', '.join(backToStr(odd))}")
