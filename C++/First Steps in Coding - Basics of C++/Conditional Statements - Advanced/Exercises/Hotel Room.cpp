#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;
int main() {
	string month;
	int nights = 0;
	double studioPrice, apartmentPrice;
	cin >> month >> nights;
	if (month == "May" or month == "October") {
		studioPrice = 50 * nights; apartmentPrice = 65 * nights;
		if (nights > 14) {
			studioPrice -= (studioPrice*0.30);
		}
		else if (nights > 7) {
			studioPrice -= (studioPrice*0.05);
		}
	}
	else if (month == "June" or month == "September") {
		studioPrice = 75.20*nights; apartmentPrice = 68.70*nights;
		if (nights > 14) {
			studioPrice -= (studioPrice*0.20);
		}
	}
	else if (month == "July" or month == "August") {
		studioPrice = 76 * nights; apartmentPrice = 77*nights;
	}
	if (nights > 14) {
		apartmentPrice -= (apartmentPrice * 0.10);
	}

	cout << fixed << setprecision(2) << "Apartment: " << apartmentPrice << " lv."<< endl;
	cout << fixed << setprecision(2) << "Studio: " << studioPrice << " lv.";
}