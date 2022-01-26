#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	string animal;
	cin >> animal;
	if (animal == "dog") {
		cout << "mammal";
	}
	else if (animal == "tortoise" or animal == "crocodile" or animal == "snake") {
		cout << "reptile";
	}
	else {
		cout << "unknown";
	}
	return 0;
}