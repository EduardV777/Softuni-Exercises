#include <iostream>
#include <string>
using namespace std;

int main() {
	int width, len, height, space;
	bool freeSpace = true;
	cin >> width; cin >> len; cin >> height;
	space = width * len*height;
	while (true) {
		if (space <= 0) {
			freeSpace = false;
			break;
		}
		string boxes;
		getline(cin >> ws, boxes);
		if (boxes != "Done") {
			int boxesCount = stoi(boxes);
			space -= boxesCount;
		}
		else {
			break;
		}
	}
	if (freeSpace == true) {
		cout << space << " Cubic meters left.";
	}
	else {
		cout << "No more free space! You need " << abs(space) << " Cubic meters more.";
	}
}
