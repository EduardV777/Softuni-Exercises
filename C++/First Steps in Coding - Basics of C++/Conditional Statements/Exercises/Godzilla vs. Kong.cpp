#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;
int main() {
	double filmBudget, extras, extrasClothesPrice;
	cin >> filmBudget; cin >> extras; cin >> extrasClothesPrice;
	double decorCost = filmBudget * 0.1, extrasClothesCost = extrasClothesPrice * extras;
	if (extras > 150) {
		extrasClothesCost -= (extrasClothesCost * 0.1);
	}
	if (decorCost + extrasClothesCost > filmBudget) {
		cout << fixed << setprecision(2) << "Not enough money!\n Wingard needs " << (decorCost + extrasClothesCost) - filmBudget << " leva more.";
	}
	else {
		cout << fixed << setprecision(2) << "Action!\n Wingard starts filming with " << filmBudget - (decorCost + extrasClothesCost) << " leva left.";
	}
}