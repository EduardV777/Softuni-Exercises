#include <iostream>
#include <set>

using namespace std;

void ShowSet(set<int> someSet) {
	for (int n : someSet) {
		cout << n << ", ";
	}
	cout << endl << endl;
}

int main() {
	cout << "\nCreating a set...\n\n";
	set<int> numSet = { 7,1,8,2,4 };

	cout << "Size of set: " << numSet.size() << "\n\n";
	for (int n : numSet) {
		cout << n << ", ";
	}
	cout << endl << endl;
	cout << "Removing value - 4\n\n";
	ShowSet(numSet);
	cout << "Inserting a value - 10\n\n";
	numSet.insert(10);
	ShowSet(numSet);
	//numSet.clear();
	cout << "Is the set empty? - " << numSet.empty() << endl << endl;
	cout << "Seeking element - 7\n\n";
	auto res = numSet.find(7);
	//auto res = numSet.find(11);
	if (res != numSet.end()) {
		cout << "Value: " << *res;
	}
	else {
		cout << "Value not found!";
	}
	return 0;
}