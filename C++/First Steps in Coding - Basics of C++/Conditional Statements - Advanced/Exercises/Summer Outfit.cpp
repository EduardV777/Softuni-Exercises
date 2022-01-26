#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	int deg;
	string daytime, outfit, shoes;
	cin >> deg >> daytime;
	if (daytime == "Morning") {
		if (10 <= deg and deg <= 18) {
			outfit = "Sweatshirt"; shoes = "Sneakers";
		}
		else if (18 < deg and deg <= 24) {
			outfit = "Shirt"; shoes = "Moccasins";
		}
		else if (deg >= 25) {
			outfit = "T-Shirt"; shoes = "Sandals";
		}
	}
	else if (daytime == "Afternoon") {
		if (10 <= deg and deg <= 18) {
			outfit = "Shirt"; shoes = "Moccasins";
		}
		else if (18 < deg and deg <= 24) {
			outfit = "T-Shirt"; shoes = "Sandals";
		}
		else if (deg >= 25) {
			outfit = "Swim Suit"; shoes = "Barefoot";
		}
	}
	else if (daytime == "Evening") {
		if (10 <= deg and deg <= 18) {
			outfit = "Shirt"; shoes = "Moccasins";
		}
		else if (18 < deg and deg <= 24) {
			outfit = "Shirt"; shoes = "Moccasins";
		}
		else if (deg >= 25) {
			outfit = "Shirt"; shoes = "Moccasins";
		}
	}
	cout << "It's " << deg << " degrees, get your " << outfit << " and " << shoes << ".";
}