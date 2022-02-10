#include <cstdlib>
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main() {
	string studentName;
	int terminated = 0, k=1;
	double gradesSum = 0;
	getline(cin, studentName);
	while (k <= 12) {
		double grade;
		cin >> grade;
		if (grade < 4.00) {
			terminated += 1;
			if (terminated > 1) {
				cout << studentName << " has been excluded at " << k << " grade";
				break;
			}
		}
		else {
			gradesSum += grade;
			if (k == 12) {
				cout << fixed << setprecision(2) << studentName << " graduated. Average grade: " << gradesSum / 12;
			}
			k++;
		}
	}
}
