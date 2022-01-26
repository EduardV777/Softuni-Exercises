#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int number; 
	double bonusPts = 0;
	cin >> number;
	if (number <= 100) {
		bonusPts += 5;
	}
	else if (number>100 && number<=1000) {
		bonusPts += number * 0.2;
	}
	else if (number > 1000) {
		bonusPts += number * 0.1;
	}
	if (number % 2 == 0) {
		bonusPts += 1;
	}else if (number % 5 == 0) {
		bonusPts += 2;
	}
	cout << bonusPts << "\n" << bonusPts + number;
}