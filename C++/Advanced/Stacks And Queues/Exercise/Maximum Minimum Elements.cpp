#include <iostream>
#include <cstdlib>
#include <stack>
#include <string>
#include <climits>
using namespace std;

void ProcessStackQueries(stack<int>& numbers, int n) {
	while (n != 0) {
		string query;
		getline(cin >> ws, query);
		if (query[0] == '1') {
			string x = "";
			for (int k = 2; k < query.length(); k++) {
				x += query[k];
			}
			numbers.push(stoi(x));
		}
		else if (query[0] == '2') {
			if (!numbers.empty()) {
				numbers.pop();
			}
		}
		else if (query[0] == '3') {
			int maxNum = INT_MIN;
			if (!numbers.empty()) {
				stack<int>copy = numbers;
				while (!copy.empty()) {
					if (maxNum < copy.top()) {
						maxNum = copy.top();
					}
					copy.pop();
				}
				cout << maxNum << "\n";
			}
		}
		else if (query[0] == '4') {
			int minNum = INT_MAX;
			if (!numbers.empty()) {
				stack<int>copy = numbers;
				while (!copy.empty()) {
					if (minNum > copy.top()) {
						minNum = copy.top();
					}
					copy.pop();
				}
				cout << minNum << "\n";
			}
		}
		n--;
	}
	while (!numbers.empty()) {
		cout << numbers.top();
		if (numbers.size() != 1) {
			cout << ", ";
		}
		numbers.pop();
	}
}


int main() {
	stack<int> numbers;
	int n;
	cin >> n;
	ProcessStackQueries(numbers, n);
	return 0;
}