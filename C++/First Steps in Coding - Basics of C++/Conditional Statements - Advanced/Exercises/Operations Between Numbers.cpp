#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	int num1, num2;
	string op;
	cin >> num1 >> num2 >> op;
	if (op == "+") {
		cout << num1 << " " << op << " " << num2 << " = " << num1 + num2 << " - ";
		if ((num1 + num2) % 2 == 0) {
			cout << "even";
		}
		else {
			cout << "odd";
		}
	}
	else if (op == "-") {
		cout << num1 << " " << op << " " << num2 << " = " << num1 - num2 << " - ";
		if ((num1 - num2) % 2 == 0) {
			cout << "even";
		}
		else {
			cout << "odd";
		}
	}
	else if (op == "*") {
		cout << num1 << " " << op << " " << num2 << " = " << num1 * num2 << " - ";
		if ((num1 * num2) % 2 == 0) {
			cout << "even";
		}
		else {
			cout << "odd";
		}
	}
	else if (op == "/") {
		if (num2 == 0) {
			cout << "Cannot divide " << num1 << " by zero";
		}
		else {
			cout << fixed << setprecision(2) << num1 << " " << op << " " << num2 << " = " << (double)num1 / num2;
		}
	}
	else if (op == "%") {
		if (num2 == 0) {
			cout << "Cannot divide " << num1 << " by zero";
		}
		else {
			cout << num1 << " " << op << " " << num2 << " = " << num1 % num2;
		}
	}
	return 0;
}