#include <iostream>
#include <cstdlib>
#include <stack>

using namespace std;

int main() {
	stack<int> numbers;
	numbers.push(25);
	numbers.push(34);
	numbers.push(12);
	numbers.push(98);
	numbers.emplace(777);

	while (!numbers.empty()) {
		cout << "Last number: " << numbers.top() << endl;
		numbers.pop();
	}
	cout << endl << endl << "End of program!";
	return 0;
}