from packages import Triangle
while True:
    try:
        s = int(input())
        break
    except ValueError:
        print("Invalid number")

Triangle.print_triangle(s)