decorations = int(input())
daysLeft = int(input())


christmasExpense = 0
christmasSpirit = 0


for k in range(1, daysLeft + 1):
    expenses = 0
    points = 0

    if k % 11 == 0: #Increasing the quantity of decorations by 2 every 11th day
        decorations += 2

    if k % 2 == 0:      #Ornament Sets - $2 - 5points
        expenses = decorations * 2
        points += 5

    if k % 3 == 0:      #Tree skirts and Tree garlands ($5/3)($3/10)
        expenses += (decorations * 5) + (decorations * 3)
        points += 3 + 10

    if k % 5 == 0:      #Tree lights - $15 - 17points
        expenses += decorations * 15
        points += 17

        if k % 3 == 0:
            points += 30

    if k % 10 == 0: #Cat ruins all decorations, leads to losing points
        christmasSpirit -= 20
        expenses += 5 + 3 + 15

        if k == daysLeft:   #The cat demolishes even more which leads to losing more points in case it is both 10th day and last day
            christmasSpirit -= 30

    christmasExpense += expenses
    christmasSpirit += points


print(f"Total cost: {christmasExpense}\nTotal spirit: {christmasSpirit}")