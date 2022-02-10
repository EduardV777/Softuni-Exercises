#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;
int main() {
	int n, k=0;
	cin >> n;
	while (k<n) {
		int number = 2 * k + 1;
		k = number;
		if (number <= n) {
			cout << number << endl;
		}
	}
}
