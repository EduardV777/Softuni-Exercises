#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {
	list<int> numbers;
	list<int> results;
	string values, curr = "";
	getline(cin >> ws, values);

	for (signed int k = 0; k <= values.length(); k++) {
		if (k == values.length() || values[k] == ' ') {
			numbers.push_back(stoi(curr));
			curr = "";
		}
		else {
			curr += values[k];
		}
	}

	while (numbers.size()) {
		int res = numbers.front();
		numbers.pop_front();
		if (numbers.size() != 0) {
			res += numbers.back();
			numbers.pop_back();
		}
		results.push_back(res);
	}

	while (results.size()) {
		cout << results.front() << " ";
		results.pop_front();
	}
	return 0;
}