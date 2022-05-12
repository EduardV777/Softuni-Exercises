#include <iostream>
#include <cstdlib>
#include <stack>
#include <string>

using namespace std;

void loadClothes(stack<int>& clothes, string clothesStr) {
	string numRep = "";
	for (int k = 0; k <= clothesStr.length(); k++) {
		if (clothesStr[k] == ' ' || k == clothesStr.length()) {
			clothes.push(stoi(numRep));
			numRep = "";
			continue;
		}
		else {
			numRep += clothesStr[k];
		}
	}
}

void HangClothes(stack<int> clothes, int rackCapacity, int& usedRacks) {
	int sumCap = 0;
	if (rackCapacity > 0) {
		while (!clothes.empty()) {
			if (sumCap + clothes.top() == rackCapacity) {
				sumCap = 0;
				clothes.pop();
				if (clothes.size() > 0) {
					usedRacks += 1;
				}
				continue;
			}
			else if (sumCap + clothes.top() > rackCapacity) {
				usedRacks += 1;
				sumCap = 0;
				continue;
			}
			else {
				sumCap += clothes.top();
			}
			clothes.pop();
		}
	}
	else {
		usedRacks -= 1;
	}
}

int main() {
	stack<int> clothes;
	string clothesInt;
	int rackCap, usedRacks = 1;
	getline(cin >> ws, clothesInt);
	cin >> rackCap;
	loadClothes(clothes, clothesInt);
	HangClothes(clothes, rackCap, usedRacks);
	cout << usedRacks;
	return 0;
}