#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

void ProcessString(string text) {
	string nonMagicalItem = "";
	for (int k = 0; k < text.length(); k++) {
		if (text[k]!=nonMagicalItem[0] || (text[k]=='a' || text[k]=='e' || text[k]=='u' || text[k]=='i' || text[k]=='o')) {
			cout << text[k];
			nonMagicalItem = text[k];
		}
	}
}

int main() {
	string txt;
	getline(cin, txt);
	ProcessString(txt);
	return 0;
}
