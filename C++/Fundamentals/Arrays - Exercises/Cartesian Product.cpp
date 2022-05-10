#include <iostream>

using namespace std;


int* CreateArray(int sizeEntry) {
	int* arr = new int[sizeEntry];
	for (int k = 0; k < sizeEntry; k++) {
		cin >> arr[k];
	}
	return arr;
}

int* CalcResult(int* array, int sizeEntry) {
	int* newArr = new int[50];
	int i = 0, currNum=0;
	for (int k = 0; k < sizeEntry; k++) {
		currNum = array[k];
		for (int j = 0; j < sizeEntry; j++) {
			newArr[i] = array[j] * currNum;
			i++;
		}
	}
	newArr[i] = -777;
	return newArr;
}

void printArray(int* array, int sizeEntry=50) {
	for (int t = 0; t < sizeEntry; t++) {
		if (array[t] == -777) {
			break;
		}
		cout << array[t] << " ";
	}
}

int main() {
	int size, * arr, *resArr;
	cin >> size;
	arr = CreateArray(size);
	resArr = CalcResult(arr, size);
	printArray(resArr);
	return 0;
}
