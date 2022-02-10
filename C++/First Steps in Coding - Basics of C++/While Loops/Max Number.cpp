#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;
int main() {
	int maxNum, k=0;
	while (true) {
		string currNum;
		cin >> currNum;
		if (currNum=="Stop"){
			cout << maxNum;
			break;
		}
		else {
			int number = stoi(currNum);
			if (k == 0) {
				maxNum = number;
				k++;
			}
			if (maxNum < number) {
				maxNum = number;
			}
		}
	}
}
