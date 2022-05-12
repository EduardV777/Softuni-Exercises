#include <iostream>
#include <cstdlib>
#include <queue>
#include <climits>

using namespace std;

int findX(queue<int>& numbers, int x) {
	int smallestNumber = INT_MAX;
	while (!numbers.empty()) {
		if (numbers.front() == x) {
			return INT_MAX;
		}
		else if (smallestNumber > numbers.front()) {
			smallestNumber = numbers.front();
		}
		numbers.pop();
	}
	return smallestNumber;
}

int main() {
	int n, s, x, k = 0;
	queue<int> numbers;
	cin >> n >> s >> x;
	while (k < n) {
		int number;
		cin >> number;
		numbers.push(number);
		k++;
	}
	k = 0;
	while (k < s) {
		numbers.pop();
		k++;
	}
	if (numbers.size() != 0) {
		int res = findX(numbers, x);
		if (res == INT_MAX) {
			cout << "true";
		}
		else {
			cout << res;
		}
	}
	else {
		cout << 0;
	}

	return 0;
}