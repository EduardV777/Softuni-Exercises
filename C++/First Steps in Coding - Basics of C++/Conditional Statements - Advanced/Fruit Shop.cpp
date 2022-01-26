#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	string fruit, day;
	double qty, price;
	getline(cin, fruit); getline(cin, day); cin >> qty;
	if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday") {
		if (fruit == "banana") {
			price = 2.50;
		}
		else if (fruit == "apple") {
			price = 1.20;
		}
		else if (fruit == "orange") {
			price = 0.85;
		}
		else if (fruit == "grapefruit") {
			price = 1.45;
		}
		else if (fruit == "kiwi") {
			price = 2.70;
		}
		else if (fruit == "pineapple") {
			price = 5.50;
		}
		else if (fruit == "grapes") {
			price = 3.85;
		}
		else {
			price = -1;
		}
	}
	else if (day == "Saturday" or day == "Sunday") {
		if (fruit == "banana") {
			price = 2.70;
		}
		else if (fruit == "apple") {
			price = 1.25;
		}
		else if (fruit == "orange") {
			price = 0.90;
		}
		else if (fruit == "grapefruit") {
			price = 1.60;
		}
		else if (fruit == "kiwi") {
			price = 3.00;
		}
		else if (fruit == "pineapple") {
			price = 5.60;
		}
		else if (fruit == "grapes") {
			price = 4.20;
		}
		else {
			price = -1;
		}
	}
	else {
		price = -1;
	}
	if (price != -1) {
		cout << fixed << setprecision(2) << qty * price;
	}
	else {
		cout << "error";
	}
}