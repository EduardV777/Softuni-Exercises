#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;
//in 212 20 2
// out 5
int main() {
	int pages, pagesPerHour, daysToRead;
	cin >> pages; cin >> pagesPerHour; cin >> daysToRead;
	int hoursNeeded = (pages/pagesPerHour)/daysToRead;
	cout << hoursNeeded;
}