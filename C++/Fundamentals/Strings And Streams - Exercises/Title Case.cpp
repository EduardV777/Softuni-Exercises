#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

string UpperCaseString(string text) {
	bool newWord = true;
	for (int k = 0; k < text.length(); k++) {
		if (!(int(text[k]) >= 65 && int(text[k])<=90) && !((int(text[k]) >= 97 && int(text[k])<=122))) {
			newWord = true;
		}
		if ((int(text[k]) >= 65 && int(text[k]) <= 90) || (int(text[k])>=97 && int(text[k])<=122)) {
			if (newWord == true) {
				newWord = false;
				if(int(text[k])>=97 && int(text[k])<=122){
					int charCode = int(text[k]);
					charCode -= 32;
					text[k] = char(charCode);
				}
			}
		}
	}
	return text;
}
int main() {
	string text;
	getline(cin, text);
	text = UpperCaseString(text);
	cout << text;
	return 0;
}
