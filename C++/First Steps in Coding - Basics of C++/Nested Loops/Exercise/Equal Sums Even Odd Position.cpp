#include <iostream>
using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	for (int k = a; k <= b; k++) {
		int evenNumSum = 0, oddNumSum=0;
		int hThousands = k / 100000 % 10, tThousands = k / 10000 % 10, Thousands = k / 1000 % 10, Hundreds = k / 100 % 10, Tenths = k / 10 % 10, Units=k%10;
		evenNumSum = tThousands + Hundreds + Units;
		oddNumSum = hThousands + Thousands + Tenths;
		if (evenNumSum == oddNumSum) {
			cout << k << " ";
		}
	}
}
