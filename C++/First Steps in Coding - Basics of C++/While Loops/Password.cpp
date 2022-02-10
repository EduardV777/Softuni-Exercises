#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;
int main() {
	string accName, passw;
	getline(cin, accName); getline(cin, passw);
	while (true) {
		string loginPass;
		getline(cin, loginPass);
		if (loginPass != passw) {
			continue;
		}
		else {
			cout << "Welcome " << accName << "!";
			break;
		}
	}
}
