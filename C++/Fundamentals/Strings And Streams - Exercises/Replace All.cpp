#include <iostream>
#include <string>
using namespace std;

string ReplaceFragments(string text, string fragment, string replacement) {
	while (true) {
		int pos = text.find(fragment), fragmentLen=fragment.length();
		if (pos == 4294967295 || pos < 0) {
			break;
		}
		text.replace(pos, fragmentLen, replacement);
	}
	return text;
}

int main() {
	string text, findTxt, replaceTxt;
	getline(cin, text);
	getline(cin>>ws, findTxt);
	getline(cin>>ws, replaceTxt);
	text = ReplaceFragments(text, findTxt, replaceTxt);
	cout << text;
	return 0;
}
