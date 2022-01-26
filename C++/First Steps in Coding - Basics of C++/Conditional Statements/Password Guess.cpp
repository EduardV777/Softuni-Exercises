#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	string pass, phrase = "s3cr3t!P@ssw0rd";
	cin >> pass;
	if (pass == phrase) {
		cout << "Welcome";
	}
	else {
		cout << "Wrong password!";
	}
}