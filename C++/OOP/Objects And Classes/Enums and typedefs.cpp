#include <iostream>

using namespace std;

int main() {
	enum types { low = 2, medium = 4, high = 6 };
	types lowVar = low;
	cout << lowVar << endl << endl;

	typedef int customType;

	customType num = 340;

	cout << num << endl << endl;

	using customType2 = int;

	customType2 num2 = 1024;

	cout << num2;
	return 0;
}