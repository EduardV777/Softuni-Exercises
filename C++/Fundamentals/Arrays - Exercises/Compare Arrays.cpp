#include <iostream>

using namespace std;


bool areEqual(int* array1, int size1, int* array2, int size2) {
	if (size1 != size2) {
		return false;
	}

	for (int k = size1; k < size1; k++) {
		if (array1[k] != array2[k]) {
			return false;
		}
	}
	return true;
}

int* CreateArrays(int sizeEntry) {
	int size=sizeEntry, *arr;
	arr = new int[size];
	for (int k = 0; k < size; k++) {
		cin >> arr[k];
	}
	return arr;
}

int main() {
	int* ar1, * ar2;
	int sizeAmount1, sizeAmount2;
	cin >> sizeAmount1;
	ar1 = CreateArrays(sizeAmount1);
	cin >> sizeAmount2;
	ar2 = CreateArrays(sizeAmount2);
	if (areEqual(ar1, sizeAmount1, ar2, sizeAmount2)) {
		cout << "equal";
	}
	else {
		cout << "Not equal";
	}
	return 0;
}
