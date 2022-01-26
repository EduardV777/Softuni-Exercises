#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	string day;
	cin >> day;
	if (day == "Monday" or day=="Tuesday" or day=="Friday") {
		cout << "12";
	}
	else if (day == "Wednesday" or day=="Thursday") {
		cout << "14";
	}
	else if (day=="Saturday" or day=="Sunday") {
		cout << "16";
	}
}