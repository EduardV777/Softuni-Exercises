#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
using namespace std;
int main() {
	int examHour, examMinutes, arrivalHour, arrivalMinutes, hours=0, minutes=0;
	cin >> examHour >> examMinutes >> arrivalHour >> arrivalMinutes;
	
	examHour *= 60; examHour += examMinutes;
	arrivalHour *= 60; arrivalHour += arrivalMinutes;
	//late
	if (examHour < arrivalHour) {
		cout << "Late\n";
		if (arrivalHour - examHour >= 60) {
			arrivalHour -= examHour;
			hours = floor(arrivalHour / 60);
			arrivalHour -= (60 * hours);
			minutes = arrivalHour;
			cout << hours << ":";
			if (minutes < 10) {
				cout << "0" << minutes;
			}
			else {
				cout << minutes;
			}
			cout << " hours after the start";
		}
		else {
			cout << arrivalHour - examHour << " minutes after the start";
		}
	}
	//on time
	else if ((examHour==arrivalHour) or (examHour-arrivalHour<=30)) {
		if (examHour == arrivalHour) {
			cout << "On time";
		}
		else {
			cout << "On time\n"<<examHour-arrivalHour<<" minutes before the start";
		}
	}
	//early
	else if (examHour-arrivalHour>30) {
		if (examHour - arrivalHour < 60) {
			cout << "Early\n" << examHour - arrivalHour << " minutes before the start";
		}
		else {
			examHour -= arrivalHour;
			hours = floor(examHour / 60);
			examHour -= (60 * hours);
			minutes = examHour;
			cout << "Early\n" << hours << ":";
			if (minutes < 10) {
				cout << "0" << minutes;
			}
			else {
				cout << minutes;
			}
			cout << " hours before the start";
		}
	}
}