#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

int main() {
	double holidayCost, jigsawPrice = 2.60, talkingDollPrice = 3, teddyBearPrice = 4.10, minionPrice = 8.20, truckPrice = 2, earnings;
	int orderedToys=0, jigsawsOrdered, dollsOrdered, bearsOrdered, minionsOrdered, trucksOrdered;
	cin >> holidayCost;
	cin >> jigsawsOrdered;
	cin >> dollsOrdered;
	cin >> bearsOrdered;
	cin >> minionsOrdered;
	cin >> trucksOrdered;
	earnings = (jigsawsOrdered * jigsawPrice) + (dollsOrdered * talkingDollPrice) + (bearsOrdered * teddyBearPrice) + (minionsOrdered * minionPrice) + (trucksOrdered * truckPrice);
	orderedToys += jigsawsOrdered + dollsOrdered + bearsOrdered + minionsOrdered + trucksOrdered;
	if (orderedToys >= 50) {
		earnings -= earnings * 0.25;
	}
	earnings -= earnings * 0.1;
	if (earnings >= holidayCost) {
		earnings -= holidayCost;
		cout << fixed << setprecision(2) << "Yes! " << earnings << " lv left.";
	}
	else {
		double needed = holidayCost - earnings;
		cout << fixed << setprecision(2) << "Not enough money! " << needed << " lv needed.";
	}
}