#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	for (int k = 1111; k <= 9999; k++) {
		int Thousands = k/1000 % 10, Hundreds=k/100%10, Tenths=k/10%10, Units=k%10;
		if (Hundreds == 0 or Tenths == 0 or Units == 0) {
			continue;
		}
		if (n%Thousands == 0 and n%Hundreds == 0 and n%Tenths == 0 and n%Units == 0) {
			cout << k << " ";
		}
	}
}
