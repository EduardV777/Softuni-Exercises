#include <iostream>
#include <string>

using namespace std;

void ShowArray(string** arr, int r, int c) {
	cout << endl << endl;
	for (signed int k = 0; k < r; k++) {
		for (signed int j = 0; j < c; j++) {
			cout << arr[k][j];
		}
		cout << endl;
	}
}


string ReturnPositions(string** arr, int r, int c, string elementToSearch) {
	string output = "";
	for (signed int k = 0; k < r; k++) {
		for (signed int j = 0; j < c; j++) {
			if (arr[k][j] == elementToSearch) {
				output += to_string(k) + " " + to_string(j) + "\n";
			}
		}
	}

	if (output == "") {
		return "not found";
	}
	else {
		return output;
	}
}

int main() {
	string sizes, val = "", lookFor;
	int r = 0, c = 0;
	getline(cin >> ws, sizes);

	for (signed int k = 0; k <= sizes.length(); k++) {
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

	string** nums = new string * [r];

	for (signed int row = 0; row < r; row++) {
		nums[row] = new string[c];
		string values;
		getline(cin >> ws, values);
		for (int k = 0, i = 0; k <= values.length(); k++) {
			if (k == values.length() || values[k] == ' ') {
				nums[row][i] = val;
				val = "";
				i++;
			}
			else {
				val += values[k];
			}
		}
	}
	//ShowArray(nums, r, c);

	getline(cin >> ws, lookFor);

	cout << ReturnPositions(nums, r, c, lookFor);
	return 0;
}