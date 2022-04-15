#include <iostream>
#include <string>
using namespace std;

string ReturnNoise(string text) {
	string noiseString = "", returnNoise="";
	bool newNoise = false, empty=true;
	int maxLen = 0;
	for (int unsigned k = 0; k <= text.length(); k++) {
		if (k == text.length() || text[k] == ' ') {
			newNoise = true;
		}
		if (newNoise == true) {
			if (maxLen < noiseString.length()) {
				maxLen = noiseString.length();
			}
			if (returnNoise.length() == 0) {
				returnNoise = noiseString;
				empty = false;
			}
			if (empty == false) {
				if (int(returnNoise[0]) > int(noiseString[0]) && noiseString.length()==maxLen) {
					returnNoise = noiseString;
				}
			}
			newNoise = false;
			noiseString = "";
		}
		if (k != text.length()) {
			if (!(text[k] >= '0' && text[k] <= '9') && text[k]!=' ') {
				noiseString += text[k];
			}
		}
	}
	return returnNoise;
}


int main() {
	string Noise;
	getline(cin, Noise);
	Noise = ReturnNoise(Noise);
	if (Noise.length() > 0) {
		cout << Noise;
	}
	else {
		cout << "no noise";
	}
	return 0;
}
