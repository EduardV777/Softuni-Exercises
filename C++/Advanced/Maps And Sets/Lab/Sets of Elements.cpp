#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
	set<int> col1;
	set<int> col2;
	set<int> uniques;
	int n, m;
	cin >> n >> m;
	while (n != 0) {
		int num;
		cin >> num;
		col1.insert(num);
		n--;
	}
	while (m != 0) {
		int num;
		cin >> num;
		col2.insert(num);
		m--;
	}

	for (int num : col1) {
		for (int num2 : col2) {
			if (num == num2) {
				uniques.insert(num);
				break;
			}
		}
	}

	for (int e : uniques) {
		cout << e << " ";
	}
	return 0;
}