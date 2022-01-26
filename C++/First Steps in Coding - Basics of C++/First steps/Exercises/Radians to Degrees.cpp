#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

int main() {
	double rad, deg, pi=3.14;
	cin >> rad;
	deg = rad * (180 / pi);
	cout << round(deg);
}