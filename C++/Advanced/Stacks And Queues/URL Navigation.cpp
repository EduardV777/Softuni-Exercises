//make simple url navigation with a stack and some commands like /back

#include <iostream>
#include <cstdlib>
#include <stack>
#include <string>

using namespace std;

void readCommand(stack<string>& history) {
	string comm;
	getline(cin >> ws, comm);
	if (!history.empty()) {
		if (comm == "/back") {
			cout << "Last Page: " << history.top() << "\n";
			history.pop();
		}
		else if (comm == "end") {
			while (!history.empty()) {
				history.pop();
			}
		}
		else {
			cout << "Last Page: " << history.top() << "\n";
			history.push(comm);
		}
		if (!history.empty()) {
			cout << "\nCurrent Page: " << history.top() << "\n";
		}
	}
}

int main() {
	stack<string> BrowserHistory;
	BrowserHistory.push("Home");
	while (!BrowserHistory.empty()) {
		readCommand(BrowserHistory);
	}

	cout << "\n\nBrowser closed!";
	return 0;
}