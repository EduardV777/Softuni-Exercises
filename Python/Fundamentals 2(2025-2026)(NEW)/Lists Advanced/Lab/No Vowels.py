# 'a', 'o', 'u', 'e', 'i'.

txt = input()

txt = [k for k in txt]

vowels = ['a', 'o', 'u', 'e', 'i']

#remove vowels, case insensitive

txt = [k for k in txt if not k.lower() in vowels]

print(''.join(txt))