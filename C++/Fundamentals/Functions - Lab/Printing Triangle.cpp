#include <iostream>
using namespace std;

void PrintTriangle(int n, bool backwards=false) {
	if (backwards == true) {
		for (int k = n - 1; k > 0; k--) {
			int j = 1;
			while (j <= k) {
				cout << j;
				if (j != k) {
					cout << " ";
				}
				j++;
			}
			cout << endl;
		}
		return;
	}
	for (int k = 1; k <= n; k++) {
		int j = 1;
		while (j <= k) {
			cout << j;
			if (j != k) {
				cout << " ";
			}
			j++;
		}
		cout << endl;
	}
	PrintTriangle(n, true);
}

int main() {
	int n;
	cin >> n;
	PrintTriangle(n);
	return 0;
}
