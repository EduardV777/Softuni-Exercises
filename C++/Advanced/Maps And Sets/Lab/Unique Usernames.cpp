#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
	set<string> usernames;
	int n;
	cin >> n;
	while (n != 0) {
		string user;
		getline(cin >> ws, user);
		usernames.insert(user);
		n--;
	}

	for (string u : usernames) {
		cout << u << "\n";
	}
	return 0;
}