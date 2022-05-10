#include <iostream>
#include <cstdlib>
#include <stack>
#include <string>

using namespace std;

string WordsStream(string CurrStream) {
	string word;
	getline(cin >> ws, word);
	if (word == "end") {
		cout << endl << endl << endl;
		return "end";
	}
	CurrStream += word; CurrStream += " ";
	return CurrStream;
}


int main() {
	string StringWords = "", word = "";
	stack<string> words;

	while (true) {
		string res = WordsStream(StringWords);
		if (res != "end") {
			StringWords = res;
		}
		else {
			break;
		}
	}

	for (int k = 0; k < StringWords.length(); k++) {
		if (StringWords[k] == ' ' || k == StringWords.length()) {
			words.push(word);
			word = "";
		}
		else {
			word += StringWords[k];
		}
	}

	while (!words.empty()) {
		cout << words.top() << " ";
		words.pop();
	}

	cout << endl << endl << "End of program!\n";
	return 0;
}