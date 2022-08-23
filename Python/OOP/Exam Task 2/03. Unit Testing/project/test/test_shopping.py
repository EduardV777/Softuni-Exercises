from project.shopping_cart import ShoppingCart
import unittest

class Tests(unittest.TestCase):
    def test_init(self):
        shoppingCart = ShoppingCart("HopShop", 10)
        self.assertEqual(shoppingCart.shop_name, "HopShop")
        self.assertEqual(shoppingCart.budget, 10)

        with self.assertRaises(ValueError) as err:
            shoppingCart = ShoppingCart("hOpShop3", 10)

        self.assertEqual(str(err.exception), "Shop must contain only letters and must start with capital letter!")

        shoppingCart = ShoppingCart("HopShop", 400)
        res = shoppingCart.add_to_cart("produkt", 99)
        self.assertEqual(res, "produkt product was successfully added to the cart!")

        shoppingCart = ShoppingCart("HopShop", 400)
        with self.assertRaises(ValueError) as err:
            res = shoppingCart.add_to_cart("produkt", 200)
        self.assertEqual(str(err.exception), "Product produkt cost too much!")

        shoppingCart = ShoppingCart("HopShop", 400)
        shoppingCart.add_to_cart("carrots", 5)
        shoppingCart.add_to_cart("parrots", 25)
        res = shoppingCart.remove_from_cart("carrots")
        self.assertEqual(res, "Product carrots was successfully removed from the cart!")
        self.assertNotIn("carrots", shoppingCart.products)
        self.assertIn("parrots", shoppingCart.products)

        with self.assertRaises(ValueError) as err:
            res = shoppingCart.remove_from_cart("t-shirts")
        self.assertEqual(str(err.exception), "No product with name t-shirts in the cart!")


        shop1 = ShoppingCart("Eddyshop", 500)
        shop1.add_to_cart("pizza", 30)
        shop1.add_to_cart('burger', 20)
        shop2 = ShoppingCart("HopShop", 400)
        shop2.add_to_cart("wrench", 10)
        resultingShop = shop1 + shop2
        self.assertEqual(resultingShop.__class__.__name__, 'ShoppingCart')
        self.assertEqual(resultingShop.shop_name, "EddyshopHopShop")
        self.assertEqual(resultingShop.budget, 900)
        prodDict = {'pizza': 30, 'burger': 20, 'wrench': 10}
        self.assertEqual(resultingShop.products, prodDict)

        shoppingCart = ShoppingCart("HopShop", 400)
        shoppingCart.add_to_cart("clothes", 45)
        shoppingCart.add_to_cart("cleaning equipment", 20)

        res = shoppingCart.buy_products()
        self.assertEqual(res, 'Products were successfully bought! Total cost: 65.00lv.')

        shoppingCart.add_to_cart("toys", 99)
        shoppingCart.add_to_cart("car parts", 99)
        shoppingCart.add_to_cart("house tools", 99)
        shoppingCart.add_to_cart("power outlets", 99)

        with self.assertRaises(ValueError) as err:
            res = shoppingCart.buy_products()
        self.assertEqual(str(err.exception), "Not enough money to buy the products! Over budget with 61.00lv!")