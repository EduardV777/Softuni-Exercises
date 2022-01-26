#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	int num;
	cin >> num;
	switch (num) {
	case 0:
		cout << "No";
		break;
	default:
		if (num <= 100 and num >= -100) {
			cout << "Yes";
		}
		else {
			cout << "No";
		}
	}
}