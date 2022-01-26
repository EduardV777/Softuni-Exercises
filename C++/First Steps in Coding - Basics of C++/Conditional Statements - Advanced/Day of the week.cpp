#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int num;
	cin >> num;
	if (num<1 or num>7) {
		cout << "Error";
	}
	else {
		if (num == 1) {
			cout << "Monday";
		}
		else if (num == 2) {
			cout << "Tuesday";
		}
		else if (num == 3) {
			cout << "Wednesday";
		}
		else if (num == 4) {
			cout << "Thursday";
		}
		else if (num == 5) {
			cout << "Friday";
		}
		else if (num == 6) {
			cout << "Saturday";
		}
		else if (num == 7) {
			cout << "Sunday";
		}
	}
	return 0;
}