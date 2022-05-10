#include <iostream>
using namespace std;
int main() {
	int a,b,k=10, div1=0, div2=-1;
	cin >> a >> b;

	while (k) {
		if (a%k == 0) {
			div1 = k;
		}
		if (b%k == 0) {
			div2 = k;
		}
		if (div1 == div2) {
			break;
		}
		k--;
	}
	if (a == b) {
		cout << a;
	}
	else {
		cout << div1;
	}
	return 0;
}
