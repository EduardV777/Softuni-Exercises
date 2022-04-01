#include <iostream>
using namespace std;
int main() {
	int n, min=0, max=0;
	cin >> n;
	while (n) {
		int num;
		cin >> num;
		if (min == 0 && max == 0) {
			min = num; max = num;
		}
		else {
			if (max < num) {
				max = num;
			}
			else if (min > num) {
				min = num;
			}
		}
		n--;
	}
	cout << min << " " << max;
	return 0;
}
