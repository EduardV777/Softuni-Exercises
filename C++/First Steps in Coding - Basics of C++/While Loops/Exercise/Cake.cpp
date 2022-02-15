#include <iostream>
#include <string>
using namespace std;

int main() {
	int width, len, cakePieces, missingPieces;
	bool cakeLeft = true;
	cin >> width; cin >> len;
	cakePieces = width * len;
	while (cakePieces > 0) {
		if (cakePieces <= 0) {
			cakeLeft = false;
			break;
		}
		string takenPieces;
		getline(cin >> ws, takenPieces);
		if (takenPieces != "STOP") {
			int takenPiecesCount = stoi(takenPieces);
			if (takenPiecesCount > cakePieces) {
				missingPieces = takenPiecesCount - cakePieces;
				cakeLeft = false;
				break;
			}
			cakePieces -= takenPiecesCount;
		}
		else {
			if (cakePieces <= 0) {
				cakeLeft = false;
			}
			break;
		}
	}
	if (cakeLeft == false) {
		cout << "No more cake left! You need " << missingPieces << " pieces more." ;
	}
	else {
		cout << cakePieces << " pieces are left.";
	}
}
