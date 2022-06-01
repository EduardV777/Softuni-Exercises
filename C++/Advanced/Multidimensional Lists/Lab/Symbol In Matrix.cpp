#include <iostream>
#include <string>

using namespace std;

void ShowArray(string** arr, int rows, int cols) {
	for (int k = 0; k < rows; k++) {
		for (int j = 0; j < cols; j++) {
			cout << arr[k][j] << " ";
		}
		cout << endl;
	}
}

string ReturnSymbolPosition(string** arr, int rows, int cols, string symbolToLookFor) {
	string positions = "(";
	bool symbolFound = false;
	for (int k = 0; k < rows; k++) {
		for (int j = 0; j < cols; j++) {
			if (arr[k][j] == symbolToLookFor) {
				positions += to_string(k) + ", " + to_string(j) + ")";
				symbolFound = true;
				break;
			}
		}
		if (symbolFound == true) {
			break;
		}
	}

	if (symbolFound == false) {
		positions = symbolToLookFor + " does not occur in the matrix";
	}
	return positions;
}

int main() {
	int n;
	cin >> n;
	string** symbols = new string * [n];

	for (int rows = 0; rows < n; rows++) {
		string symbolsToEnter;
		getline(cin >> ws, symbolsToEnter);
		symbols[rows] = new string[n];
		for (unsigned int k = 0, i = 0; k < symbolsToEnter.length(); k++) {
			symbols[rows][i] = symbolsToEnter[k];
			i++;
		}
	}
	string symbolToSearch;
	getline(cin >> ws, symbolToSearch);
	//cout << endl;
	//ShowArray(symbols, n, n);
	cout << ReturnSymbolPosition(symbols, n, n, symbolToSearch);

	return 0;
}