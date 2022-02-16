#include <iostream>
#include <string>
using namespace std;
int main() {
	int floors, roomsPerFloor, floorNumber;
	cin >> floors; cin >> roomsPerFloor;
	floorNumber = floors;
	string** building = new string* [floors];
	for (int k = 0; k < floors; k++) {
		building[k] = new string[roomsPerFloor];
	}

	for (int k = 0; k < floors; k++) {
		for (int j = 0; j < roomsPerFloor; j++) {
			string floorN = to_string(floorNumber), roomN=to_string(j);
			if (floorNumber == floors) {
				building[k][j] = "L"+floorN+roomN;
			}
			else if (floorNumber % 2 == 0) {
				building[k][j] = "O"+floorN + roomN;
			}
			else if (floorNumber % 2 != 0) {
				building[k][j] = "A"+floorN + roomN;
			}
		}
		cout << endl;
		floorNumber -= 1;
	}
	
	for (int k = 0; k < floors; k++) {
		for (int j = 0; j < roomsPerFloor; j++) {
			cout << building[k][j] << " ";
		}
		cout << endl;
	}
}
