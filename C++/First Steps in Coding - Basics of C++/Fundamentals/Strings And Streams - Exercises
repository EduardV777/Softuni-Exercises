#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int* CreateArray(string numbers) {
	int* arr = new int[50];
	int i = 0;
	string currNumber = "";
	for (int k = 0; k < numbers.length(); k++) {
		if (numbers[k] == ' ') {
			arr[i] = stoi(currNumber);
			currNumber = "";
			i++;
		}
		if (int(numbers[k]) >= 48 || int(numbers[k]) <= 57) {
			currNumber += numbers[k];
		}
	}
	arr[i] = -777;
	return arr;
}

bool CompareArrays(int* arr1, int* arr2) {
	int size1=0, size2=0;
	for (int q=0; q < 50; q++) {
		if (arr1[q] == -777) {
			break;
		}
		size1 += 1;
	}
	for (int q=0; q < 50; q++) {
		if (arr2[q] == -777) {
			break;
		}
		size2 += 1;
	}

	if (size1 != size2) {
		return false;
	}
	for (int k = 0; k < 50; k++) {
		if (arr1[k] != arr2[k]) {
			return false;
		}
	}
	return true;
}

int main() {
	string numbers1, numbers2;
	int* array1, *array2;
	getline(cin, numbers1);
	array1 = CreateArray(numbers1);
	getline(cin >> ws, numbers2);
	array2 = CreateArray(numbers2);
	if (CompareArrays(array1, array2)) {
		cout << "equal";
	}
	else {
		cout << "not equal";
	}
}
