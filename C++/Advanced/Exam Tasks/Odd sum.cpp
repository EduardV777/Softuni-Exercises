#include <iostream>
#include <string>
#include <queue>

using namespace std;

void ShowArr(int** arr2D, int s) {
	for (int k = 0; k < s; k++) {
		for (int j = 0; j < s; j++) {
			cout << arr2D[k][j] << " ";
		}
		cout << endl;
	}
}

int returnOddSum(int** arr2D, int s, int& sumVar) {
	int j2 = s - 1;
	for (int k = 0; k < s; k++, j2--) {
		for (int j = 0; j < s; j++) {
			if ((j != k && j != j2) && arr2D[k][j] % 2 != 0) {
				sumVar += arr2D[k][j];
			}
		}
	}

	return sumVar;
}


int main() {
	queue<int> numbersToAdd;
	int d, dCounter, sum = 0, i = 0, col = 0;
	string numbers;
	cin >> d;
	getline(cin >> ws, numbers);

	int** numbersArr = new int* [d];
	dCounter = d;

	while (dCounter != 0) {
		numbersArr[i] = new int[d];
		dCounter--, i++;
	}

	i = 0;
	string currVal = "";
	for (int k = 0; k <= numbers.length(); k++) {
		if (k == numbers.length() || numbers[k] == ' ') {
			numbersToAdd.push(stoi(currVal));
			currVal = "";
		}
		else {
			currVal += numbers[k];
		}
	}

	while (true) {
		if (numbersToAdd.empty()) {
			break;
		}
		if (col == d) {
			col = 0;
			i++;
		}
		int number = numbersToAdd.front();
		numbersArr[i][col] = number;
		numbersToAdd.pop();
		col++;
	}

	//ShowArr(numbersArr, d);
	cout << "The sum is: " << returnOddSum(numbersArr, d, sum);
	return 0;
}