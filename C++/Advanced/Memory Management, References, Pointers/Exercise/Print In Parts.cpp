#include <iostream>
#include <string>
using namespace std;

void ShowArray(int** arr, int r, int c) {
	cout << endl << endl;
	for (signed int k = 0; k < r; k++) {
		for (signed int j = 0; j < c; j++) {
			cout << arr[k][j] << " ";
		}
		cout << endl;
	}
}

void getSizes(string values, int& r, int& c) {
	string val = "";
	for (int k = 0; k <= values.length(); k++) {
		if (k == values.length() || values[k] == ' ') {
			if (r == 0) {
				r = stoi(val);
			}
			else {
				c = stoi(val);
			}
			val = "";
		}
		else {
			val += values[k];
		}
	}
}


int main() {
	int** arr;
	int r = 0, c = 0;
	string sizes;
	getline(cin >> ws, sizes);
	getSizes(sizes, r, c);

	arr = new int* [r];
	for (int k = 0; k < r; k++) {
		string values, curr = "";
		arr[k] = new int[c];
		getline(cin >> ws, values);
		for (int j = 0, i = 0; j <= values.length(); j++) {
			if (j == values.length() || values[j] == ' ') {
				arr[k][i] = stoi(curr);
				i++;
				curr = "";
			}
			else {
				curr += values[j];
			}
		}
	}
	string showSizes;
	getline(cin >> ws, showSizes);
	int n = 0, n1;
	getSizes(showSizes, n, n1);
	ShowArray(arr, n, n1);

	return 0;
}