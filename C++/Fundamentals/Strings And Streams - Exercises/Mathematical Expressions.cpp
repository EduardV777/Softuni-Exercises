#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

bool CheckExpressionValidity(string mathExpr) {
	int unclosedBrackets = 0;
	for (int k = 0; k < mathExpr.length(); k++) {
		if (mathExpr[k] == '(') {
			unclosedBrackets++;
		}
		else if(mathExpr[k] == ')') {
			unclosedBrackets--;
		}
		if (unclosedBrackets < 0) {
			break;
		}
	}
	if(unclosedBrackets>0 || unclosedBrackets<0){
		return false;
	}
	return true;
}

int main() {
	string mathExpr;
	getline(cin, mathExpr);
	if (CheckExpressionValidity(mathExpr)) {
		cout << "correct";
	}
	else {
		cout << "incorrect";
	}
	return 0;
}
