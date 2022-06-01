def rectangle(length, width):
    output=""
    if type(length)!=int or type(width)!=int:
        return "Enter valid values!"
    def area():
        return f"Rectangle area: {length*width}"
    def perimeter():
        return f"Rectangle perimeter: {length * 2 + width * 2}"
    output=area()+"\n"
    output+=perimeter()
    return output


print(rectangle('2', 10))