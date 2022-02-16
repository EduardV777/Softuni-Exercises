#include <iostream>
using namespace std;
int main() {
	int a = 1;
	for (; a <= 10; a++) {
		for (int b=1; b <= 10; b++) {
			cout << a << " * " << b << " = " << a * b << endl;
		}
	}
	return 0;
}
