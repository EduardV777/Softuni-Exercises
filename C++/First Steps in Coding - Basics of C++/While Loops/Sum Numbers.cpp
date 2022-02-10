#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;
int main() {
	int initNum, res=0;
	cin >> initNum;
	while (res < initNum) {
		int number;
		cin >> number;
		res += number;
	}
	cout << res;
}
