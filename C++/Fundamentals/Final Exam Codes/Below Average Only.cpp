#include <iostream>
#include <cstdlib>
using namespace std;

int* CreateArray(int size, double& avg) {
	int* arr = new int[size];
	for (int k = 0; k < size; k++) {
		cin >> arr[k];
		avg += arr[k];
	}
	avg /= size;
	return arr;
}

void CountOddEven(int* arr, int size, int &var1, int &var2, double average) {
	for (int k = 0; k < size; k++) {
		if (arr[k] <= average) {
			if (k % 2 == 0) {
				var1 += arr[k];
			}
			else {
				var2 += arr[k];
			}
		}
	}
}

int main() {
	int* seq, size, countEven=0, countOdd=0; 
	double avg = 0;
	cin >> size;
	seq=CreateArray(size, avg);
	CountOddEven(seq, size, countEven, countOdd, avg);
	cout << countEven * countOdd;
	return 0;
}
