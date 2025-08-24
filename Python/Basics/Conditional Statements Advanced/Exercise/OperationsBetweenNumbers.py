n1 = int(input())
n2 = int(input())
operator = input() # +, -, *, /, %
output = ""

if operator == "+" or operator == "-" or operator == "*":

    output = f"{n1} {operator} {n2} = {eval(f'{n1}{operator}{n2}')}"

    even = eval(f"{n1}{operator}{n2}") % 2

    if even == 0:
        output += " - even"
    else:
        output += " - odd"

elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        output = f"{n1} {operator} {n2} = {eval(f'{n1}{operator}{n2}'):.2f}"

elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        output = f"{n1} {operator} {n2} = {eval(f'{n1}{operator}{n2}')}"


print(output)