#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;
int main() {
	while (true) {
		string text;
		getline(cin, text);
		if (text != "Stop") {
			cout << text << endl;
		}
		else {
			break;
		}
	}
}
