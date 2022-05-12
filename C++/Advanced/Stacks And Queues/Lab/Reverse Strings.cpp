#include <iostream>
#include <cstdlib>
#include <stack>
#include <string>
using namespace std;

string reverseString(string str) {
	stack<string> reverseStack;
	string word = "", reversedString = "";
	for (int k = 0; k <= str.length(); k++) {
		if (str[k] == ' ' || k == str.length()) {
			reverse(word.begin(), word.end());
			word += " ";
			reverseStack.push(word);
			word = "";
		}
		else {
			word += str[k];
		}
	}
	while (!reverseStack.empty()) {
		reversedString += reverseStack.top();
		reverseStack.pop();
	}
	return reversedString;
}

int main() {
	string str;
	getline(cin >> ws, str);
	cout << reverseString(str);
	return 0;
}