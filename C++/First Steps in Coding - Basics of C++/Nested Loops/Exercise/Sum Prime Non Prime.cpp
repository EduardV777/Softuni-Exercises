#include <iostream>
#include <string>
using namespace std;

int main() {
	int primeSum = 0, nonPrimeSum = 0;
	while (true) {
		string number;
		getline(cin, number);
		if (number != "stop") {
			int num = stoi(number);
			bool prime = false;
			if (num < 0) {
				cout << "Number is negative." << endl;
				continue;
			}
			for (int k = 1; k <= 10; k++) {
				if (k == 1 or k == num) {
					continue;
				}
				if (num%k == 0) {
					prime = true;
					break;
				}
			}
			if (prime == false) {
				nonPrimeSum += num;
			}
			else {
				primeSum += num;
			}
		}
		else {
			cout << "Sum of all prime numbers is: " << nonPrimeSum << "\nSum of all non prime numbers is: " << primeSum;
			break;
		}
	}
}
