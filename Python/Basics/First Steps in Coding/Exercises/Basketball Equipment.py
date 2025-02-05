basketBallYearlyTax = float(input())

sneakersPrice = basketBallYearlyTax - basketBallYearlyTax * 0.4
jerseyPrice = sneakersPrice - sneakersPrice * 0.2
ballPrice = jerseyPrice / 4
accessoriesPrice = ballPrice / 5

trainingCosts = basketBallYearlyTax + sneakersPrice + jerseyPrice + ballPrice + accessoriesPrice

print(trainingCosts)