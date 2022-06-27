def shopping_cart(*args):
    emptyMealProducts = 0

    cart = {'Soup': [], 'Pizza': [], 'Dessert': []}

    for k in range(0,len(args)):

        if args[k] == 'Stop':
            break

        if args[k][0] == 'Soup':
            if len(cart['Soup']) < 3:
                if args[k][1] not in cart['Soup']:
                    cart['Soup'].append(args[k][1])
        
        elif args[k][0] == 'Pizza':
            if len(cart['Pizza']) < 4:
                if args[k][1] not in cart['Pizza']:
                    cart['Pizza'].append(args[k][1])
        
        elif args[k][0] == 'Dessert':
            if len(cart['Dessert']) < 2:
                if args[k][1] not in cart['Dessert']:
                    cart['Dessert'].append(args[k][1])

    for meal in cart:
        if len(cart[meal]) <= 0:
            emptyMealProducts += 1

    if emptyMealProducts == 3:
        return "No products in the cart!"

    sortCart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))
    
    sortCart = dict(sortCart)

    output = ""

    for meal in sortCart:
        output += f"{meal}:\n"

        sortCart[meal].sort()

        for product in sortCart[meal]:
            output += f" - {product}\n"
    
    return output







print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

"""
Soup: 3
Pizza: 4
Dessert: 2
"""