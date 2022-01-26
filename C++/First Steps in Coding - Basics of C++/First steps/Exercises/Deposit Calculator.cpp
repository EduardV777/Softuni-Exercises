#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

int main() {
	double depositedSum, rate, finalSum;
	int months;
	cin >> depositedSum; cin >> months; cin >> rate;
	rate /= 100;
	finalSum = depositedSum + months * ((depositedSum * rate) / 12);
	cout << fixed << setprecision(2) << finalSum;
	return 0;
}