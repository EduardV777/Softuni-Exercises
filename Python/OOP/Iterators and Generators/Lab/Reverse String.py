def reverse_text(text):
    return (ch for ch in reversed(text))

for char in reverse_text("step"):
    print(char, end='')