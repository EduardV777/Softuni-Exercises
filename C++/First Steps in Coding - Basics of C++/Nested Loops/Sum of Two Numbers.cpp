#include <iostream>
using namespace std;
int main() {
	int beg, end, magicNumber, combNum=0;
	bool foundComb = false;
	cin >> beg; cin >> end; cin >> magicNumber;
	for (int k = beg; k <= end; k++) {
		for (int j = beg; j <= end; j++) {
			if (k + j == magicNumber) {
				combNum += 1;
				cout << "Combination N:" << combNum << " (" << k << " + " << j << " = " << magicNumber << ")";
				foundComb = true;
				break;
			}
			else {
				combNum += 1;
			}
		}
		if (foundComb == true) {
			break;
		}
	}
	if (foundComb == false) {
		cout << combNum << " combinations - neither equals " << magicNumber;
	}
}
