#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;

bool IsItNumber(string text) {
	bool number = false;
	for (int k = 0; k < text.length(); k++) {
		if ((text[k]>='0' && text[k]<='9') || text[k]=='-') {
			number = true;
		}
	}
	return number;
}

int main() {
	vector<int> numbers;
	while (true) {
		string op;
		getline(cin >> ws, op);
		bool isItNum = IsItNumber(op);
		if (isItNum) {
			int number = stoi(op);
			numbers.push_back(number);
		}
		else {
			if (op == "sum") {
				if (numbers.size() > 1) {
					int num1 = numbers[numbers.size()-1], num2=numbers[numbers.size()-2], i=2;
					while (i != 0) {
						numbers.pop_back();
						i--;
					}
					numbers.push_back(num1 + num2);
				}
			}
			else if (op == "subtract") {
				if (numbers.size() > 1) {
					int num1 = numbers[numbers.size() - 1], num2 = numbers[numbers.size() - 2], i = 2;
					while (i != 0) {
						numbers.pop_back();
						i--;
					}
					numbers.push_back(num1 - num2);
				}
			}
			else if (op == "concat") {
				if (numbers.size() > 1) {
					string num1 = to_string(numbers[numbers.size() - 1]), num2 = to_string(numbers[numbers.size() - 2]), finalNumber=num2+num1;
					int i = 2;
					while (i != 0) {
						numbers.pop_back();
						i--;
					}
					numbers.push_back(stoi(finalNumber));
				}
			}
			else if (op == "discard") {
				numbers.pop_back();
			}
			else if(op=="end") {
				break;
			}
		}
	}
	for (int k = 0; k < numbers.size(); k++) {
		cout << numbers[k] << endl;
	}
	return 0;
}
