#include <iostream>
#include <string>
using namespace std;

int FindMaximumNumber(string text) {
	bool newNoise = false;
	string number = "";
	int max = 0;
	for (int k = 0; k < text.length(); k++) {
		if (text[k] == ' ') {
			newNoise = true;
		}
		if (newNoise == true) {
			if (max < stoi(number)) {
				max = stoi(number);
			}
			number = "";
			newNoise = false;
		}
		if (text[k] >= '0' && text[k] <= '9') {
			number += text[k];
		}
	}
	if (max < stoi(number)) {
		max = stoi(number);
	}
	return max;
}

int main() {
	string NoisyNumbers;
	getline(cin, NoisyNumbers);
	int maxNum = FindMaximumNumber(NoisyNumbers);
	cout << maxNum;
	return 0;
}
