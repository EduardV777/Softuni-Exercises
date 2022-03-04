countries=input(); capitals=input()
countries=countries.split(", "); capitals=capitals.split(", ")

countriesCapitals={country:capital for (country,capital) in zip(countries,capitals)}
for j in countriesCapitals:
    print(f"{j} -> {countriesCapitals[j]}")
