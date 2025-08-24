txt = input()
values = [1,2,3,4,5]  #a e i o u
vowels = ["a", "e", "i", "o", "u"]
val = 0

for k in range(0, len(txt)):
    if txt[k] in vowels:
        val += values[vowels.index(txt[k])]

print(val)
