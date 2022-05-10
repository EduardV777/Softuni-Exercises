#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>
using namespace std;

int FindNum(string theNoise) {
	string number="";
	for (int k = 0; k < theNoise.length(); k++) {
		if (int(theNoise[k]) >= 48 && int(theNoise[k]) <= 57) {
			number += theNoise[k];
		}
	}
	return stoi(number);
}

int main() {
	string noisyNum, txt="0";
	int actualNum;
	getline(cin, noisyNum);
	actualNum = FindNum(noisyNum);
	cout << sqrt(actualNum);
	return 0;
}
