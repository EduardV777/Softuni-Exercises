txt = input().split(" ")

txt = [k for k in txt if len(k) % 2 == 0]; txt = "\n".join(txt)

print(txt)