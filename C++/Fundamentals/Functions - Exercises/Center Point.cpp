#include <iostream>

using namespace std;

int main() {
	double a, b, c, d, x1,y1,x2,y2;
	cin >> a >> b >> c >> d;
	x1 = a; y1 = b; x2 = c; y2 = d;
	if (a < 0) {
		a *= -1;
	}
	if (b < 0) {
		b *= -1;
	}
	if (c < 0) {
		c *= -1;
	}
	if (d < 0) {
		d *= -1;
	}
	double dest1 = a + b, dest2=c+d;
	if (dest1 < dest2) {
		cout << "(" << x1 << ", " << y1 << ")";
	}
	else if (dest2 < dest1) {
		cout << "(" << x2 << ", " << y2 << ")";
	}
	else {
		cout << "(" << x1 << ", " << y1 << ")";
	}
	return 0;
}
