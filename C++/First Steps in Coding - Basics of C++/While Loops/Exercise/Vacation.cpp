#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
	int daysSpending = 0, totalDays=0;
	double requiredMoney, availableMoney;
	cin >> requiredMoney; cin >> availableMoney;
	while (true) {
		string action;
		cin >> action;
		if (action == "spend") {
			double sum; cin >> sum;
			if (sum >= availableMoney) {
				availableMoney = 0;
			}
			else {
				availableMoney -= sum;
			}
			daysSpending += 1;
		}
		else if (action == "save") {
			daysSpending = 0;
			double sum; cin >> sum;
			availableMoney += sum;
		}
		totalDays += 1;
		if (daysSpending == 5) {
			cout << "You can't save the money.\n" << totalDays;
			break;
		}
		if (availableMoney >= requiredMoney) {
			cout << "You saved the money for " << totalDays << " days.";
			break;
		}
	}
}
