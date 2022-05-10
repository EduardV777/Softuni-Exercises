#include <iostream>
using namespace std;
int main() {
	double grade;
	cin >> grade;
	if (grade >= 2.00 && grade <= 2.99) {
		cout << "Fail";
	}
	else if (grade >= 3.00 && grade <= 3.49) {
		cout << "Poor";
	}
	else if (grade >= 3.50 && grade <= 4.49) {
		cout << "Good";
	}
	else if (grade >= 4.50 && grade <= 5.49) {
		cout << "Very good";
	}
	else if (grade >= 5.50 && grade <= 6.00) {
		cout << "Excellent";
	}
	return 0;
}
