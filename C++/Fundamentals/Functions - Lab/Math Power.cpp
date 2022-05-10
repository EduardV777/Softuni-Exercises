#include <iostream>
using namespace std;

int PowerNumber(int num, int exp) {
	int k = 1, res=num;
	while (k < exp) {
		res *= num;
		k++;
	}
	if (exp == 0 && num!=0) {
		return 1;
	}
	else if (exp == 0 && num == 0) {
		return 0;
	}
	else {
		return res;
	}
}

int main() {
	int a,b;
	cin >> a >> b;
	cout << PowerNumber(a, b);
	return 0;
}
