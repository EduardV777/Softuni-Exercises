#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	double age;
	string sex;
	cin >> age >> sex;
	if (sex == "m" && age >= 16) {
		cout << "Mr.";
	}
	else if (sex == "m" && age < 16) {
		cout << "Master";
	}
	else if (sex == "f" && age >= 16) {
		cout << "Ms.";
	}
	else if (sex == "f" && age < 16) {
		cout << "Miss";
	}
	return 0;
}