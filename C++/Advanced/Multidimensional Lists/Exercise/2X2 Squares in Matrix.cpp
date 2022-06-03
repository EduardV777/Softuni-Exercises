#include <iostream>
#include <string>

using namespace std;

void ShowArray(string** arr, int r, int c) {
	cout << endl << endl;
	for (int k = 0; k < r; k++) {
		for (int j = 0; j < c; j++) {
			cout << arr[k][j] << " ";
		}
		cout << endl;
	}
}

int find2X2(string** arr, int r, int c) {
	int sqMatrices = 0;
	int k = 0, col = 0;
	while (true) {
		if (col + 1 >= c) {
			col = 0;
			k++;
		}

		if (k + 1 >= r) {
			break;
		}

		if (arr[k][col] == arr[k + 1][col] && arr[k][col] == arr[k][col + 1] && arr[k][col] == arr[k + 1][col + 1]) {
			sqMatrices += 1;
		}
		col++;
	}
	return sqMatrices;
}


int main() {
	string sizes, val = "";
	int r = 0, c = 0;
	getline(cin >> ws, sizes);

	for (int k = 0; k <= sizes.length(); k++) {
		if (k == sizes.length() || sizes[k] == ' ') {
			if (r == 0) {
				r = stoi(val);
			}
			else {
				c = stoi(val);
			}
			val = "";
		}
		else {
			val += sizes[k];
		}
	}
	string** chars = new string * [r];
	for (signed int row = 0; row < r; row++) {
		chars[row] = new string[c];
		string values;
		getline(cin >> ws, values);
		for (signed int k = 0, i = 0; k <= values.length(); k++) {
			if (k == values.length() || values[k] == ' ') {
				chars[row][i] = val;
				i++;
				val = "";
			}
			else {
				val += values[k];
			}
		}
	}

	//ShowArray(chars, r, c);

	cout << find2X2(chars, r, c);

	return 0;
}