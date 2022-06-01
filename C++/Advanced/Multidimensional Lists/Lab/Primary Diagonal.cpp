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
	int n;
	cin >> n;
	int** multiNums = new int* [n];
	for (int rows = 0; rows < n; rows++) {
		string values, num = "";
		getline(cin >> ws, values);
		multiNums[rows] = new int[n];
		int i = 0;
		for (int k = 0; k <= values.length(); k++) {
			if (values[k] == ' ' || k == values.length()) {
				multiNums[rows][i] = stoi(num);
				num = "";
				i++;
			}
			else {
				num += values[k];
			}
		}
	}

	//ShowArray(multiNums, n, n);
	int primaryDiagonalSum = 0;

	for (int k = 0; k < n; k++) {
		primaryDiagonalSum += multiNums[k][k];
	}
	cout << primaryDiagonalSum;
	return 0;
}