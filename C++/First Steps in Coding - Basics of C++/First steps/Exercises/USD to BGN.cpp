#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

int main() {
	double usd, bgn, fixedRate=1.79549;
	cin >> usd;
	bgn = usd * fixedRate;
	cout << fixed << setprecision(2) << bgn;
}