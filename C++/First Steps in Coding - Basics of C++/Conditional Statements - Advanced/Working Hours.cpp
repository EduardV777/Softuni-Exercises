#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	int hour;
	string day;
	cin >> hour; cin >> day;
	if (hour >= 10 and hour < 18) {
		if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday") {
			cout << "open";
		}
		else {
			cout << "closed";
		}
	}
	else {
		cout << "closed";
	}
}