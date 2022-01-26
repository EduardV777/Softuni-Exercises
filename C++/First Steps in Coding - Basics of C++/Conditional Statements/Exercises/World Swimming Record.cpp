#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
using namespace std;
int main() {
	double recordToBeat, distance, swimSecPerM;
	int slowedTimes=0;
	cin >> recordToBeat; cin >> distance; cin >> swimSecPerM;
	slowedTimes = floor(distance / 15);
	double slowDownTime = 12.5 * slowedTimes;
	double personalTime = (distance * swimSecPerM)+slowDownTime;
	if (personalTime < recordToBeat) {
		cout << fixed << setprecision(2) << "Yes, he succeeded! The new world record is " << personalTime << " seconds.";
	}
	else {
		cout << fixed << setprecision(2) << "No, he failed! He was " << personalTime - recordToBeat << " seconds slower.";
	}
}