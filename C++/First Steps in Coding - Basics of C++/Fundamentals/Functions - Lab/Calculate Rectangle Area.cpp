#include <iostream>
using namespace std;

int CalculateRectArea(int s1, int s2) {
	int res = s1 * s2;
	return res;
}

int main() {
	int a,b;
	cin >> a >> b;
	cout << CalculateRectArea(a, b);
	return 0;
}
