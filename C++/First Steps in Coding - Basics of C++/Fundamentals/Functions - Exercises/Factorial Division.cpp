#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
	double a, b, j=1;
	cin >> a >> b;
	while (j < 3) {
		double num, k=1, res=1;
		if (j == 1) {
			num = a;
		}
		else {
			num = b;
		}
		while (k <= num) {
			res *= k;
			k++;
		}
		if (num == a) {
			a = res;
		}
		else if (num==b) {
			b = res;
		}
		j++;
	}
	cout << fixed << setprecision(2) << a / b;
}
