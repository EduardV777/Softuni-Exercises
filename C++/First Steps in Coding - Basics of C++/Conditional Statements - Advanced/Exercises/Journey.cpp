#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	string season, dest, willStayAt;
	double spent=0, budget;
	cin >> budget >> season;
	if (budget <= 100) {
		dest = "Somewhere in Bulgaria";
		if (season == "summer") {
			spent = budget * 0.3;
			willStayAt = "Camp";
		}
		else if (season == "winter") {
			spent = budget * 0.7;
			willStayAt = "Hotel";
		}
	}
	else if (budget <= 1000) {
		dest = "Somewhere in Balkans";
		if (season == "summer") {
			spent = budget * 0.4;
			willStayAt = "Camp";
		}
		else if (season == "winter") {
			spent = budget * 0.8;
			willStayAt = "Hotel";
		}
	}
	else if (budget > 1000) {
		dest = "Somewhere in Europe";
		willStayAt = "Hotel";
		spent = budget * 0.9;
	}
	cout << fixed << setprecision(2) << dest << "\n" << willStayAt << " - " << spent;
}