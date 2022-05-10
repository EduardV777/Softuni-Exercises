#include <iostream>
using namespace std;
int main() {
	int num;
	cin >> num;
	if (num < 0) {
		cout << "The number " << num << " is negative.";
	}
	else if (num > 0) {
		cout << "The number " << num << " is positive.";
	}
	else {
		cout << "The number " << num << " is zero.";
	}
	return 0;
}
