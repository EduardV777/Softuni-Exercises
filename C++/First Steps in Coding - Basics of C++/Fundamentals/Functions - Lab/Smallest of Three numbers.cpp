#include <iostream>
using namespace std;
int FindSmallest() {
	int k = 3, min;
	while (k) {
		int num;
		cin >> num;
		if (k == 3) {
			min = num;
		}
		else {
			if (min > num) {
				min = num;
			}
		}
		k--;
	}
	return min;
}

int main() {
	cout<<FindSmallest();
	return 0;
}
