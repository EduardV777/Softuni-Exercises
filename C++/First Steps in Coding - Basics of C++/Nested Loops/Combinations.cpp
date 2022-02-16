#include <iostream>
using namespace std;
int main() {
	int validCombs = 0, n;
	cin >> n;
	for (int k = 0; k <= 25; k++) {
		for (int j = 0; j <= 25; j++) {
			for (int i = 0; i <= 25; i++) {
				if (k + j + i == n) {
					validCombs += 1;
				}
			}
		}
	}
	cout << validCombs;
}
