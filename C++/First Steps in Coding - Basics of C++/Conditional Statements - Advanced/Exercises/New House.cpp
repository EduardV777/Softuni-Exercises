#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	string flowerType;
	int qty;
	double budget,cost;
	cin >> flowerType >> qty >> budget;
	if (flowerType == "Roses") {
		cost = 5.00 * qty;
		if (qty > 80) {
			cost -= (cost*0.10);
		}
	}
	else if (flowerType == "Dahlias") {
		cost = 3.80*qty;
		if (qty > 90) {
			cost -= (cost*0.15);
		}
	}
	else if (flowerType == "Tulips") {
		cost = 2.80*qty;
		if (qty > 80) {
			cost -= (cost*0.15);
		}
	}
	else if (flowerType == "Narcissus") {
		cost = 3.00 * qty;
		if (qty < 120) {
			cost += (cost*0.15);
		}
	}
	else if (flowerType == "Gladiolus") {
		cost = 2.50*qty;
		if (qty < 80) {
			cost += (cost*0.20);
		}
	}
	if (cost<=budget){
		cout << fixed << setprecision(2) << "Hey, you have a great garden with " << qty << " " << flowerType << " and " << budget - cost << " leva left.";
	}
	else {
		cout << fixed << setprecision(2) << "Not enough money, you need " << cost - budget << " leva more.";
	}
}