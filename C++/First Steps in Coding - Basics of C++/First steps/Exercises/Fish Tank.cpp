#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int l, w, h;
	double space, pctTaken;
	cin >> l; cin >> w; cin >> h; cin >> pctTaken;
	space = (l * w * h) * 0.001; 
	pctTaken = space * (pctTaken / 100); 
	space = space-pctTaken;
	cout << fixed << space;
}