#include <iostream>
#include <cstdlib>
using namespace std;

int* CreateArray(int size) {
	int* arr = new int[size];
	for (int k = 0; k < size; k++) {
		cin >> arr[k];
	}
	return arr;
}

int FindClosest(int* arr, int size) {
	int currDiff = -777;
	for (int k = 0; k < size; k++) {
		for (int j = 0; j < size; j++) {
			if (j == k) {
				continue;
			}
			if (currDiff>abs(arr[k] - arr[j]) || currDiff==-777) {
				currDiff = abs(arr[k] - arr[j]);
			}
		}
	}
	if (currDiff == -777) {
		currDiff = 0;
	}
	return currDiff;
}

int main() {
	int size, *numbers;
	cin >> size;
	numbers = CreateArray(size);
	cout << FindClosest(numbers, size);
	return 0;
}
