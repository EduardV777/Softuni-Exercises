#include <iostream>

using namespace std;


int* CreateSequence(int sizeEntry) {
	int* arr = new int[sizeEntry];
	for (int k = 0; k < sizeEntry; k++) {
		cin >> arr[k];
	}
	return arr;
}

int* CreateCounter(int* array, int sizeEntry) {
	int* counter=new int [sizeEntry*2];
	int i = 0;
	for (int k = 0; k < sizeEntry * 2; k++) {
		if ((k+1) % 2 == 0) {
			counter[k] = 0;
		}
		else {
			counter[k] = -999;
		}
	}
	for (int k = 0; k < sizeEntry; k++) {
		bool exists = false;
		for (int j = 0; j < sizeEntry * 2; j += 2) {
			if (counter[j] == array[k]) {
				exists = true;
				break;
			}
		}
		if (exists==false) {
			counter[i] = array[k];
			i+=2;
		}
	}
	return counter;
}

int* ProcessArray(int* array, int* counter, int size) {
	int counterSize = size * 2, maxOccurs=0, i=0;
	int* mostFrequentNumbers=new int [20];
	for (int j = 0; j < counterSize; j += 2) {
		int currOccurs = 0;
		for (int k = 0; k < size; k++) {
			if (counter[j] == array[k]) {
				counter[j + 1] += 1;
				currOccurs += 1;
			}
		}
		if (currOccurs > maxOccurs) {
			maxOccurs = currOccurs;
		}
	}

	for (int j = 1; j < counterSize; j += 2) {
		if (counter[j] == maxOccurs) {
			mostFrequentNumbers[i] = counter[j - 1];
			i++;
		}
	}
	mostFrequentNumbers[i] = -777;
	return mostFrequentNumbers;
}

void PrintMostFrequent(int* mfArr, int size = 20) {
	//sort
	while (true) {
		int k = 0;
		bool keepSorting = false;
		for (int k = 0; k < size; k++) {
			if (mfArr[k + 1] == -777) {
				break;
			}
			if (mfArr[k] > mfArr[k + 1]) {
				keepSorting = true;
				int temp = mfArr[k];
				mfArr[k] = mfArr[k + 1];
				mfArr[k + 1] = temp;
			}
		}
		if (keepSorting == false) {
			break;
		}
	}
	//print
	for (int k = 0; k < 220; k++) {
		if (mfArr[k] == -777) {
			break;
		}
		cout << mfArr[k] << " ";
	}
}

int main() {
	int* arr, *counterArr, *resArr;
	int size;
	cin >> size;
	arr = CreateSequence(size);
	counterArr = CreateCounter(arr, size);
	resArr = ProcessArray(arr, counterArr, size);
	PrintMostFrequent(resArr);
	return 0;
}
