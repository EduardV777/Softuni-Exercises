#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int amountMarkers, amountPens, amountCleaningLiquid;
	double markersPrice = 7.20, pensPrice = 5.80, cleaningLiquidPrice = 1.20, finalSum, discount;
	cin >> amountPens; cin >> amountMarkers; cin >> amountCleaningLiquid; cin >> discount;
	finalSum = (amountPens * pensPrice) + (amountMarkers * markersPrice) + (amountCleaningLiquid * cleaningLiquidPrice);
	finalSum -= finalSum * (discount / 100);
	cout << finalSum;
}