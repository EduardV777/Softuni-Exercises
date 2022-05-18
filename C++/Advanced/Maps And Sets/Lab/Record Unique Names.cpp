#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
	set<string> uniqueNames;
	int n;
	cin >> n;
	while (n != 0) {
		string name;
		getline(cin >> ws, name);
		uniqueNames.insert(name);
		n--;
	}

	for (string k : uniqueNames) {
		cout << k << "\n";
	}
	return 0;
}