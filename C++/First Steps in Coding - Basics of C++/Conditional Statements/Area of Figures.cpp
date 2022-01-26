#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

int main() {
	string figureType; double area;
	cin >> figureType;
	if (figureType == "square") {
		double sideLen;
		cin >> sideLen;
		area = sideLen * sideLen;
	}
	else if (figureType == "rectangle") {
		double sideLen1, sideLen2;
		cin >> sideLen1; cin >> sideLen2;
		area = sideLen1 * sideLen2;
	}
	else if (figureType == "circle") {
		double r;
		cin >> r;
		area = 3.14159 * (r * r);
	}
	else if (figureType == "triangle") {
		double a, h;
		cin >> a; cin >> h;
		area = (a / 2) * h;
	}
	cout << fixed << setprecision(3) << area;
}