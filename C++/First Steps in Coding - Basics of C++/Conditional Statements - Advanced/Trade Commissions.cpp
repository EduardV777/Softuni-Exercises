//Sofia- (0<=s<=500:5%)(500<s<=1000:7%)(1000<s<=10000:8%)(s>10000:12%)
//Varna- (0<=s<=500:4.5%)(500<s<=1000:7.5%)(1000<s<=10000:10%)(s>10000:13%)
//Plovdiv- (0<=s<=500:5.5%)(500<s<=1000:8%)(1000<s<=10000:12%)(s>10000:14.5%)
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	string city;
	double sellVolume, commission;
	getline(cin, city); cin >> sellVolume;
	if (city == "Sofia") {
		if (sellVolume >= 0 && sellVolume <= 500) {
			commission = 5.0/100;
		}
		else if (sellVolume > 500 && sellVolume <= 1000) {
			commission = 7.0 / 100;
		}
		else if (sellVolume > 1000 && sellVolume <= 10000) {
			commission = 8.0 / 100;
		}
		else if (sellVolume > 10000) {
			commission = 12.0 / 100;
		}
		else {
			commission = -101;
		}
	}
	else if (city == "Varna") {
		if (sellVolume >= 0 && sellVolume <= 500) {
			commission = 4.5 / 100;
		}
		else if (sellVolume > 500 && sellVolume <= 1000) {
			commission = 7.5 / 100;
		}
		else if (sellVolume > 1000 && sellVolume <= 10000) {
			commission = 10.0 / 100;
		}
		else if (sellVolume > 10000) {
			commission = 13.0 / 100;
		}
		else {
			commission = -101;
		}
	}
	else if (city == "Plovdiv") {
		if (sellVolume >= 0 && sellVolume <= 500) {
			commission = 5.5 / 100;
		}
		else if (sellVolume > 500 && sellVolume <= 1000) {
			commission = 8.0 / 100;
		}
		else if (sellVolume > 1000 && sellVolume <= 10000) {
			commission = 12.0 / 100;
		}
		else if (sellVolume > 10000) {
			commission = 14.5 / 100;
		}
		else {
			commission = -101;
		}
	}
	else {
		commission = -101;
	}
	if (commission != -101) {
		cout << fixed << setprecision(2) << sellVolume * commission;
	}
	else {
		cout << "error";
	}
}