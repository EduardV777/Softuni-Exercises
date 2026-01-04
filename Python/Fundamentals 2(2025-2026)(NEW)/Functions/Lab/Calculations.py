def calculate(op = input(), a = int(input()), b = int(input()) ):
    res = 0

    if op == "add":
        res = a + b

    elif op == "subtract":
        res = a - b

    elif op == "multiply":
        res = a * b

    elif op == "divide":
        res = a / b

    return res

result = calculate()
print(result)