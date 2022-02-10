#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	double accBalance=0;
	while (true) {
		string command;
		cin >> command;
		if (command == "NoMoreMoney") {
			break;
		}
		else {
			double sum;
			sum = stod(command);
			if (sum < 0) {
				cout << "Invalid operation!" << endl;
				break;
			}
			else {
				accBalance += sum;
				cout << fixed << setprecision(2) << "Increase: " << sum << endl;
			}
		}
	}
	cout << fixed << setprecision(2) << "Total: " << accBalance << endl;
}
