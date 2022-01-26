#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int comp1, comp2, comp3, sumMin, sumSec;
	double sumTime;
	cin >> comp1; cin >> comp2; cin >> comp3;
	sumTime = comp1 + comp2 + comp3;
	sumMin = sumTime / 60; sumSec = sumTime - (sumMin * 60);
	if (sumSec < 10) {
		cout << sumMin << ":0" << sumSec;
	}
	else {
		cout << sumMin << ":" << sumSec;
	}
}