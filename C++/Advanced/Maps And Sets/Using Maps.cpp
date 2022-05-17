#include <utility>
#include <map>
#include <iostream>
#include <string>

using namespace std;

int main() {
	map<string, string> accounts;
	accounts.insert(pair<string, string>("Velkov", "2gfdrgsz"));
	accounts.insert(pair<string, string>("John", "99 * John"));
	accounts.insert(pair<string, string>("Admin", "root"));

	for (auto i = accounts.begin(); i != accounts.end(); i++) {
		cout << i->first << ", " << i->second << "\n";
	}
	return 0;
}