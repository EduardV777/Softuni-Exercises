#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
	set<string> parking;
	while (true) {
		//direction: in/out, number
		string data, direction, carNum, val = "";
		getline(cin >> ws, data);
		if (data != "END") {
			for (int k = 0; k <= data.length(); k++) {
				if (data[k] == ',' || k == data.length()) {
					if (direction == "") {
						direction = val;
					}
					else {
						carNum = val;
					}
					k++;
					val = "";
				}
				else {
					val += data[k];
				}
			}
			if (direction == "IN") {
				parking.insert(carNum);
			}
			else if (direction == "OUT") {
				parking.erase(carNum);
			}
		}
		else {
			if (parking.empty()) {
				cout << "Parking Lot is Empty";
			}
			else {
				for (string c : parking) {
					cout << c << "\n";
				}
				break;
			}
		}

	}
	return 0;
}