#include <iostream>
#include <string>
using namespace std;

int main() {
	int checkedBooks=0;
	string desiredBook;
	getline(cin, desiredBook);
	while (true) {
		string bookName;
		getline(cin, bookName);
		if (bookName == "No More Books") {
			cout << "The book you search is not here!\nYou checked " << checkedBooks << " books.";
			break;
		}
		if (bookName == desiredBook) {
			cout << "You checked " << checkedBooks << " books and found it.";
			break;
		}
		else {
			checkedBooks += 1;
			continue;
		}
	}
}
