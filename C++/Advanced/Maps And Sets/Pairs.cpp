#include <utility>
#include <iostream>
#include <string>

using namespace std;

int main() {
	pair<int, string> pairVar(35945213, "Eduard Velkov");
	cout << "Pair variable values: \nPhone/Name: " << pairVar.first << " - " << pairVar.second << "\n";

	cout << " --------------- \nCreate new pair\nEnter account name: ";

	string accName; int id;
	getline(cin >> ws, accName);
	cout << "\nEnter account id: ";
	cin >> id;
	pair<string, int> account;
	account.first = accName; account.second = id;
	cout << "\n\nAccount name: " << account.first << "\nID: " << account.second << "\n";
	cout << " --------------- \n";
	pair<string, string> location = { "Sofia","Nadezhda" };

	cout << location.first << ", " << location.second << endl;
	return 0;
}