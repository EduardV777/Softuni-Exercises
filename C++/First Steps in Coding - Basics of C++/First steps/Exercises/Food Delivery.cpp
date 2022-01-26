#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	double chickenMenuPrice = 10.35, fishMenuPrice=12.40, vegetarianMenuPrice = 8.15, dessertPrice, delivery = 2.50, cost;
	int amountChickenMenu, amountFishMenu, amountVegetarianMenu;
	cin >> amountChickenMenu; cin >> amountFishMenu; cin >> amountVegetarianMenu;
	cost = (amountChickenMenu * chickenMenuPrice) + (amountFishMenu * fishMenuPrice) + (amountVegetarianMenu * vegetarianMenuPrice);
	dessertPrice = cost * 0.2;
	cost += dessertPrice + delivery;
	cout << cost;
}