#include <iostream>
#include <string>
#include <cmath>
using namespace std;

void ShowArray(int** arr, int rows, int cols) {
	for (int k = 0; k < rows; k++) {
		for (int j = 0; j < cols; j++) {
			cout << arr[k][j] << " ";
		}
		cout << endl;
	}
}

int ReturnDiagonalsDiff(int** arr, int rows) {
	int diff, primary = 0, secondary = 0;
	for (int k = 0; k < rows; k++) {
		primary += arr[k][k];
	}
	for (int k = 0, i = rows - 1; k < rows; k++, i--) {
		secondary += arr[k][i];
	}

	diff = abs(primary - secondary);
	return diff;
}


int main() {
	int n;
	cin >> n;
	int** arr2D = new int* [n];
	for (int rows = 0; rows < n; rows++) {
		arr2D[rows] = new int[n];
		string values, currVal = "";
		getline(cin >> ws, values);

		for (unsigned int k = 0, i = 0; k <= values.length(); k++) {
			if (k == values.length() || values[k] == ' ') {
				arr2D[rows][i] = stoi(currVal);
				currVal = "";
				i++;
			}
			else {
				currVal += values[k];
			}
		}
	}
	//cout << endl;
	//ShowArray(arr2D, n, n);
	cout << ReturnDiagonalsDiff(arr2D, n);
	return 0;
}