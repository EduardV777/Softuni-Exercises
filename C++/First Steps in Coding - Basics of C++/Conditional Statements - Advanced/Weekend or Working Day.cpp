#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	string day;
	cin >> day;
	if (day == "Saturday" or day == "Sunday") {
		cout << "Weekend";
	}
	else if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday") {
		cout << "Working day";
	}
	else {
		cout << "Error";
	}
	return 0;
}