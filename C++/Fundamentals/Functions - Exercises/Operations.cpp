#include <iostream>
#include <string>
using namespace std;


int Add(int a, int b) {
	return a + b;
}
int Substract(int a, int b) {
	return a - b;
}
int Multiply(int a, int b) {
	return a * b;
}
void Divide(int a, int b) {
	if (b == 0) {
		cout << "Can't divide by zero.";
	}
	else {
		cout << a / b;
	}
}

int main() {
	int a, b;
	cin >> a >> b;
	string operation;
	getline(cin>>ws, operation);

	if (operation=="+"){
		cout<<Add(a, b);
	}
	else if (operation=="-"){
		cout<<Substract(a, b);
	}
	else if (operation=="*"){
		cout<<Multiply(a, b);
	}
	else if (operation=="/"){
		Divide(a, b);
	}
	return 0;
}
