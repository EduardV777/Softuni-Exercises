#include <iostream>
using namespace std;

int main() {
	int n, j=1;
	cin >> n;
	for (int k = 1; k <= n; k++) {
		int nums = k;
		for (; j <= n; j++) {
			if (nums == 0) {
				break;
			}
			cout << j << " ";
			nums -= 1;
		}
		cout << endl;
	}
}
