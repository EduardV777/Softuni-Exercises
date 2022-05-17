#include <utility>
#include <map>
#include <iostream>
#include <string>

using namespace std;

int main() {
	map<string, string> accounts;
	accounts.insert(pair<string, string>("Velkov", "2gfdrgsz"));
	accounts.insert(pair<string, string>("John", "99*John"));
	accounts.insert(pair<string, string>("Admin", "root"));

	for (auto i = accounts.begin(); i != accounts.end(); i++) {
		cout << i->first << ", " << i->second << "\n";
	}
	cout << "\n---------------------\nAnother way to visualize maps\n\n";
	for (pair<string, string> i : accounts) {
		cout << i.first << ", " << i.second << "\n";
	}
	cout << "\n---------------------\nSeeking account password of username 'John'...\n" << accounts["John"] << endl;
	cout << "\n[Adding new account with name 'Sec2727' and random password]\n";
	accounts["Sec2727"] = "gh9aehrg";
	cout << "\nData for account 'Sec2727':\nUsername: Sec2727, Password: " << accounts["Sec2727"] << endl;
	cout << "\nSeeking account with name 'Admin'\n";
	//find() returns iterator
	auto res = accounts.find("Admin");
	cout << "Username: " << res->first << ", " << "Password: " << res->second << endl;
	cout << "\n---------------------\nDeleting account with name 'Admin'\n\n";
	//Also possible with iterator as parameter and it is faster
	accounts.erase("Admin");
	cout << "Seeking account with name 'Admin' again\n";
	accounts.find("Admin");


	cout << "\n\nNumber of accounts registered: " << accounts.size() << "\n";
	for (auto i = accounts.begin(); i != accounts.end(); i++) {
		cout << i->first << " - " << i->second << endl;
	}
	return 0;
}