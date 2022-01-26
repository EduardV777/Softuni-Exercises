#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	string prod, city;
	double qty; double price;
	getline(cin, prod); getline(cin, city); cin >> qty;
	if (city == "Sofia") {
		if (prod == "coffee") {
			price = 0.50;
		}
		else if (prod == "water") {
			price = 0.80;
		}
		else if (prod == "beer") {
			price = 1.20;
		}
		else if (prod == "sweets") {
			price = 1.45;
		}
		else if (prod == "peanuts") {
			price = 1.60;
		}
	}
	else if (city == "Plovdiv") {
		if (prod == "coffee") {
			price = 0.40;
		}
		else if (prod == "water") {
			price = 0.70;
		}
		else if (prod == "beer") {
			price = 1.15;
		}
		else if (prod == "sweets") {
			price = 1.30;
		}
		else if (prod == "peanuts") {
			price = 1.50;
		}
	}
	else if (city == "Varna") {
		if (prod == "coffee") {
			price = 0.45;
		}
		else if (prod == "water") {
			price = 0.70;
		}
		else if (prod == "beer") {
			price = 1.10;
		}
		else if (prod == "sweets") {
			price = 1.35;
		}
		else if (prod == "peanuts") {
			price = 1.55;
		}
	}
	cout << qty * price;
	return 0;
}