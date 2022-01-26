#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	int daysToStay;
	string roomType, rating;
	double cost=0;
	cin >> daysToStay;
	getline(cin>>ws,roomType); getline(cin, rating);
	cin >> rating;
	daysToStay -= 1;
	if (roomType == "room for one person") {
		cost += 18.00*daysToStay;
	}
	else if (roomType == "apartment") {
		cost += 25.00*daysToStay;
		if (daysToStay < 10) {
			cost -= (cost*0.30);
		}
		else if (daysToStay >= 10 and daysToStay <= 15) {
			cost -= (cost*0.35);
		}
		else if (daysToStay > 15) {
			cost -= (cost*0.50);
		}
	}
	else if (roomType == "president apartment") {
		cost += 35.00*daysToStay;
		if (daysToStay < 10) {
			cost -= (cost*0.10);
		}
		else if (daysToStay >= 10 and daysToStay <= 15) {
			cost -= (cost*0.15);
		}
		else if (daysToStay > 15) {
			cost -= (cost*0.20);
		}
	}

	if (rating == "positive") {
		cost += (cost*0.25);
	}
	else if (rating == "negative") {
		cost -= (cost*0.10);
	}
	cout << fixed << setprecision(2) << cost;
}