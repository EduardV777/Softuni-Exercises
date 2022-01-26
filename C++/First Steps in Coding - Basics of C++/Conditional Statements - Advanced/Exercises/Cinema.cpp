#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	string projType;
	int rows, cols;
	double projPrice, earnings;
	getline(cin, projType); cin >> rows; cin >> cols;
	if (projType == "Premiere") {
		projPrice = 12.00;
	}
	else if (projType == "Normal") {
		projPrice = 7.50;
	}
	else if (projType == "Discount") {
		projPrice = 5.00;
	}
	earnings = (rows*cols)*projPrice;
	cout << fixed << setprecision(2) << earnings << " leva";
}