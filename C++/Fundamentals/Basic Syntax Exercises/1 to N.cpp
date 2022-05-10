#include <iostream>
using namespace std;
int main() {
	int n, k=1;
	cin >> n;
	while (k <= n) {
		cout << k;
		if (k != n) {
			cout << " ";
		}
		k++;
	}
	return 0;
}
