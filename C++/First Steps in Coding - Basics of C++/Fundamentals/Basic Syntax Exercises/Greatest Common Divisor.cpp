#include <iostream>
using namespace std;
int main() {
	int a,b,k=10, div1=0, div2=-1;
	cin >> a >> b;
	if (a != b) {
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
		if (div1 == 1 && div2 == 1) {
			cout << a << " and " << b << " are prime numbers, meaning they only divide by 1 and themselves, so their GCD is 1";
		}
		else {
			cout << div1 << " is the largest number that divides both " << a << " and " << b << " (without remainder)";
		}
	}
	else {
		cout << "Both numbers are " << a << ", so GCD is " << a;
	}
	return 0;
}
