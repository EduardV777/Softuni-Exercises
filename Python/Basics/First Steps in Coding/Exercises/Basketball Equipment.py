annualTrainingTax = int(input())

basketballSneakersPrice = annualTrainingTax - annualTrainingTax * 0.40
basketballJerseyPrice = basketballSneakersPrice - basketballSneakersPrice * 0.20
basketballBallPrice = basketballJerseyPrice / 4
basketballAccessoriesPrice = basketballBallPrice / 5


total = basketballSneakersPrice + basketballJerseyPrice + basketballBallPrice + basketballAccessoriesPrice + annualTrainingTax

print(f"{total}")