#include <iostream>

using namespace std;


int* CreateArrays(int sizeEntry) {
	int size=sizeEntry, *arr;
	arr = new int[size];
	for (int k = 0; k < size; k++) {
		cin >> arr[k];
	}
	return arr;
}

int main() {
	int num=-1, len=1, currNumber=-1, currLength = 0, * arr, sizeEntry;
	cin >> sizeEntry;
	arr = CreateArrays(sizeEntry);
	for (int k = 0; k < sizeEntry; k++) {
		if (arr[k] != currNumber) {
			currLength = 1;
			currNumber = arr[k];
		}
		else {
			currLength += 1;
		}
		if (currLength > 1) {
			num = currNumber;
			len = currLength;
		}
		/*
		if (currLength > len) {
			num = currNumber;
			len = currLength;
		}
		*/
	}
	for (int j = 0; j < len; j++) {
		if (num == -1) {
			num = arr[sizeEntry - 1];
		}
		cout << num << " ";
	}
	return 0;
}
