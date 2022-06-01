#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

void ShowArray(int** arr, int rows, int cols) {
	for (int k = 0; k < rows; k++) {
		for (int j = 0; j < cols; j++) {
			cout << arr[k][j] << " ";
		}
		cout << endl;
	}
}

int main() {
	int r = 0, c = 0;
	string matrixSizes, currVal = "";
	getline(cin >> ws, matrixSizes);

	for (int k = 0; k <= matrixSizes.length(); k++) {
		if (k == matrixSizes.length() || matrixSizes[k] == ' ') {
			if (r == 0) {
				r = stoi(currVal);
			}
			else {
				c = stoi(currVal);
			}
			currVal = "";
		}
		else {
			currVal += matrixSizes[k];
		}
	}

	//cout << r << endl << c;

	int rep = 0;
	int** multiArr = new int* [r];
	while (rep < r) {
		string rowValues, current = "";
		getline(cin >> ws, rowValues);
		multiArr[rep] = new int[c];
		for (int j = 0, i = 0; j <= rowValues.length(); j++) {
			if (j == rowValues.length() || rowValues[j] == ' ') {
				multiArr[rep][i] = stoi(current);
				i++;
				current = "";
			}
			else {
				current += rowValues[j];
			}
		}
		rep++;
	}
	cout << endl;
	//ShowArray(multiArr, r, c);

	for (int col = 0; col < c; col++) {
		int sum = 0, row = 0;
		for (; row < r; row++) {
			sum += multiArr[row][col];
		}
		cout << sum << endl;
	}
	return 0;
}