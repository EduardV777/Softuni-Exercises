#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int Hrs, Mins;
	cin >> Hrs; cin >> Mins;
	Mins += 15;
	if (Mins > 59) {
		Mins -= 60;
		Hrs += 1;
	}
	if (Hrs > 23) {
		Hrs = 0;
	}
	if (Mins < 10) {
		cout << Hrs << ":0" << Mins;
	}
	else {
		cout << Hrs << ":" << Mins;
	}
}