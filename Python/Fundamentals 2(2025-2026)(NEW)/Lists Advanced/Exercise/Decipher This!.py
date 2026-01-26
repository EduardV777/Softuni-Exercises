# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

words = input().split(" ")

def decipher(words: list):

    for j in range(0, len(words)):
        code = [k for k in words[j] if 48 <= ord(k) <= 57]
        code = int(''.join(code))

        word = [k for k in words[j] if not 48 <= ord(k) <= 57]

        word.insert(0, chr(code))
        temp = word[1]
        temp2 = word.pop(-1)
        word.append(temp)
        word[1] = temp2
        words[j] = ''.join(word)


    return ' '.join(words)


print(decipher(words))
