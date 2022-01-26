#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>
using namespace std;
int main() {
	string seriesName;
	int episodeLength, restLength;
	getline(cin, seriesName);
	cin >> episodeLength >> restLength;
	double myTime = restLength;
	double lunchTime = (double)restLength / 8, relaxTime = (double)restLength / 4;
	myTime -= lunchTime + relaxTime;
	if (myTime >= episodeLength) {
		cout << "You have enough time to watch " << seriesName << " and left with " << ceil(myTime - episodeLength) << " minutes free time.";
	}
	else {
		cout << "You don't have enough time to watch " << seriesName << ", you need " << ceil(episodeLength-myTime) << " more minutes.";
	}
	return 0;
}