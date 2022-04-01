#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main() {
	double a, b, c, D;
	cin >> a >> b >> c;
	D=b*b-(4*a*c);
	if (D < 0) {
		cout << "no roots";
	}
	else {
		if (b > 0) {
			b *= -1;
		}
		if (D == 0) {
			double x1 = b / (2 * a);
			cout << x1;
		}
		else {
			D = sqrt(D);
			double denominator = 2 * a;
			double x1 = (b + D) / denominator, x2 = (b - D) / denominator;
			if (x1 < x2) {
				double temp = x1;
				x1 = x2;
				x1 = temp;
			}
			cout << x1 << " " << x2;
		}
	}
	return 0;
}
