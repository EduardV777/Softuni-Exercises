#include <iostream>
#include <cstdlib>
#include <queue>
using namespace std;
int main() {
	priority_queue<int> elements;
	elements.push(25);
	elements.push(15);
	elements.push(45);
	elements.push(75);
	elements.push(5);
	while (elements.size() != 0) {
		cout << elements.top() << "\n";
		elements.pop();
	}
	return 0;
}