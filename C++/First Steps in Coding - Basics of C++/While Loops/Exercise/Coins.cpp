#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	double moneyChange;
	int totalCoins = 0;
	cin >> moneyChange;
	moneyChange *= 100;
	while (moneyChange != 0) {
		if (moneyChange < 1) {
			break;
		}
		if (moneyChange >= 100) {
			if (moneyChange >= 500) {
				moneyChange -= 500;
				totalCoins += 1;
			}
			else if (moneyChange >= 200) {
				moneyChange -= 200;
				totalCoins += 1;
			}
			else {
				moneyChange -= 100;
				totalCoins += 1;
			}
		}
		else {
			if (moneyChange >= 50) {
				moneyChange -= 50;
				totalCoins += 1;
			}
			else if (moneyChange >= 20) {
				moneyChange -= 20;
				totalCoins += 1;
			}
			else if (moneyChange >= 10) {
				moneyChange -= 10;
				totalCoins += 1;
			}
			else if (moneyChange >= 5) {
				moneyChange -= 5;
				totalCoins += 1;
			}
			else if (moneyChange >= 2) {
				moneyChange -= 2;
				totalCoins += 1;
			}
			else if (moneyChange >= 1) {
				moneyChange -= 1;
				totalCoins += 1;
			}
		}
		
	}
	cout << totalCoins;
	return 0;
}
