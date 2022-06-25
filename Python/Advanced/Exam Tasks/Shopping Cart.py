def shopping_cart(*args):
    arguments = args
    typeSort = "Desc"
    cartNotEmpty = False

    cart = {'Soup': [], 'Pizza': [], 'Dessert': []}

    for k in range(0,len(arguments)):
        if(arguments[k] == "Stop"):
            break

        meal = arguments[k][0]; product = arguments[k][1]

        if(meal == "Soup"):
            if(len(cart[meal]) < 3 and product not in cart[meal]):
                cart[meal].append(product)

                if(cartNotEmpty == False):
                    cartNotEmpty = True
        elif(meal == "Pizza"):
            if(len(cart[meal]) < 4 and product not in cart[meal]):
                cart[meal].append(product)

                if(cartNotEmpty == False):
                    cartNotEmpty = True
        elif(meal == "Dessert"):
            if(len(cart[meal]) < 2 and product not in cart[meal]):
                cart[meal].append(product)

                if(cartNotEmpty == False):
                    cartNotEmpty = True

    for meal in cart:

        for mealCompare in cart:
            if(meal != mealCompare and (len(cart[meal]) == len(cart[mealCompare]))):
                typeSort = "Asc"
                break

    if(typeSort == "Asc"):
        cartSort = sorted(cart.items(), key=lambda x: x[0])
    else:
        cartSort = sorted(cart.items(), key=lambda x: len(x[1]), reverse = True)


    cartSort = dict(cartSort)


    output = ""

    if(cartNotEmpty == False):
        return "No products in the cart!"
    else:
        for meal in cartSort:

            cartSort[meal].sort()

            output += f"{meal}:\n"

            for j in range(0, len(cartSort[meal])):
                output += f" - {cartSort[meal][j]}\n"

        return output

#Possible inputs
"""
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
"""

"""
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
"""


"""
print(shopping_cart(('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop'))
"""

"""
print(shopping_cart('Stop'))
"""


"""
Limitations

• Soup: 3
• Pizza: 4
• Dessert: 2

"""