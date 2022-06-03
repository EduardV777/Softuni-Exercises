#include <iostream>
#include <string>
#include <list>
using namespace std;

void ShowListReverse(list<int> seq) {
	cout << endl << endl;
	if (!seq.empty()) {
		auto k = seq.end();
		k--;
		while (true) {
			cout << *k << ' ';
			if (k == seq.begin()) {
				break;
			}
			k--;
		}
	}
	else {
		cout << "empty";
	}
}


int getSize(string e) {
	int s = 0;
	for (signed int k = 0; k <= e.length(); k++) {
		if (k == e.length() || e[k] == ' ') {
			s++;
		}
	}
	return s;
}


void RemoveNegatives(list<int>& seq) {
	auto k = seq.begin();
	while (true) {
		if (k == seq.end()) {
			break;
		}
		if (*k < 0) {
			seq.erase(k);
			k = seq.begin();
		}
		else {
			k++;
		}
	}
}

int main() {
	string elements, curr = "";
	int size;
	getline(cin >> ws, elements);
	size = getSize(elements);
	list<int> numbers;

	for (signed int k = 0; k <= elements.length(); k++) {
		if (elements[k] == ' ' || k == elements.length()) {
			numbers.push_back(stoi(curr));
			curr = "";
		}
		else {
			curr += elements[k];
		}
	}

	RemoveNegatives(numbers);
	ShowListReverse(numbers);
	return 0;
}