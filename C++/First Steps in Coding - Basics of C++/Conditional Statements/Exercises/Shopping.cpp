#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
using namespace std;
int main() {
	double videoCardPrice = 250, cpuPrice, ramPrice, requiredSum, budget;
	int videoCards, cpus, rams;
	cin >> budget; cin >> videoCards; cin >> cpus; cin >> rams;
	cpuPrice = (videoCardPrice * videoCards) * 0.35; ramPrice = (videoCardPrice * videoCards) * 0.1;
	requiredSum = (videoCards * videoCardPrice) + (cpus * cpuPrice) + (rams * ramPrice);
	if (videoCards > cpus) {
		requiredSum -= (requiredSum * 0.15);
	}
	if (requiredSum <= budget) {
		cout << fixed << setprecision(2) << "You have " << budget - requiredSum << " leva left!";
	}
	else {
		cout << fixed << setprecision(2) << "Not enough money! You need " << requiredSum - budget << " leva more!";
	}
}