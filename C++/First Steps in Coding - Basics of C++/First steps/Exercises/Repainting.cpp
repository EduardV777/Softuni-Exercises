#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	double nylonPrice=1.50, paintPrice=14.50, thinnerPrice = 5, totalCost, workersPricePerHour, paintL;
	int nylonM, thinnerL, hoursToFinish;
	cin >> nylonM; cin >> paintL; cin >> thinnerL; cin >> hoursToFinish;
	paintL += paintL * 0.10; nylonM += 2; totalCost = 0.40;
	totalCost += (nylonM * nylonPrice) + (paintL * paintPrice) + (thinnerL * thinnerPrice); 
	workersPricePerHour = (totalCost * 0.3)*hoursToFinish;
	totalCost += workersPricePerHour;
	cout << totalCost;
}