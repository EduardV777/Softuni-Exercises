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

void ProcessArray(int* array, int sizeEntry) {
	int sumAvg = 0;
	for (int j = 0; j < sizeEntry; j++) {
		sumAvg += array[j];
	}
	sumAvg /= sizeEntry;
	for (int k = 0; k < sizeEntry; k++) {
		if (array[k] >= sumAvg) {
			cout << array[k] << " ";
		}
	}
}

int main() {
	int* arr;
	int size;
	cin >> size;
	arr = CreateArrays(size);
	ProcessArray(arr, size);
	return 0;
}
