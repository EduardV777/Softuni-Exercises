countries=input()
capitals=input()
countryNames=countries.split(", ")
capitalNames=capitals.split(", ")
countryCapital=dict(zip(countryNames,capitalNames))
output=""
for k in countryCapital:
    output+=f"{k} -> {countryCapital[k]}\n"
print(output)
