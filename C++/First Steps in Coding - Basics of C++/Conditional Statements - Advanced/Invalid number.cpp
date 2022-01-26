#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	int num;
	cin >> num;
	if ((num < 100 or num > 200) and (num!=0)) {
		cout << "invalid";
	}
}