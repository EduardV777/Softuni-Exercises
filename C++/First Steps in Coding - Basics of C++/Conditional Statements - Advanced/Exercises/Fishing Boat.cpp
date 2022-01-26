#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	int groupBudget, fishermen;
	double cost=0;
	string season;
	cin >> groupBudget >> season >> fishermen;
	if (season == "Spring") {
		cost += 3000;
	}
	else if (season == "Summer" or season == "Autumn") {
		cost += 4200;
	}
	else if (season == "Winter") {
		cost += 2600;
	}

	if (fishermen <= 6) {
		cost -= (cost*0.10);
	}
	else if (fishermen >= 7 and fishermen <= 11) {
		cost -= (cost*0.15);
	}
	else if (fishermen >= 12) {
		cost -= (cost*0.25);
	}

	if (fishermen % 2 == 0 && season != "Autumn") {
		cost -= (cost*0.05);
	}

	if (cost <= groupBudget) {
		cout << fixed << setprecision(2) << "Yes! You have " << groupBudget - cost << " leva left.";
	}
	else {
		cout << fixed << setprecision(2) << "Not enough money! You need " << cost - groupBudget << " leva.";
	}
}