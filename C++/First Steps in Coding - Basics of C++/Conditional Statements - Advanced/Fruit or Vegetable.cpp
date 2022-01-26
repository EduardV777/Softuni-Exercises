#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	string prod;
	getline(cin, prod);
	if (prod == "banana" or prod == "apple" or prod == "kiwi" or prod == "cherry" or prod == "lemon" or prod == "grapes") {
		cout << "fruit";
	}
	else if (prod == "tomato" or prod == "cucumber" or prod == "pepper" or prod == "carrot") {
		cout << "vegetable";
	}
	else {
		cout << "unknown";
	}
}