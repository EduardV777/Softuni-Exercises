#include <iostream>
using namespace std;
int main() {
	int a, b, c, res=0;
	cin >> a >> b >> c;
	res = a * b*c;
	if (res < 0) {
		cout << "-";
	}
	else {
		cout << "+";
	}
	return 0;
}
