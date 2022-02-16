#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
	double standardTickets=0, studentTickets = 0, kidsTickets = 0;
	int totalTicketsSold = 0;
	while (true) {
		string movieName;
		getline(cin >> ws, movieName);
		if (movieName != "Finish") {
			double freeSeats, totalCapacity;
			bool full = true;
			cin >> freeSeats;
			totalCapacity = freeSeats;
			for (; freeSeats > 0;) {
				string ticketType;
				getline(cin >> ws, ticketType);
				if (ticketType != "End") {
					if (ticketType == "standard") {
						standardTickets += 1;
					}
					else if (ticketType == "student") {
						studentTickets += 1;
					}
					else if (ticketType == "kid") {
						kidsTickets += 1;
					}
					totalTicketsSold++; freeSeats--;
				}
				else {
					full = false;
					cout << fixed << setprecision(2) << movieName << " - " << ((totalCapacity-freeSeats) / totalCapacity)*100 << "% full." << endl;
					break;
				}
			}
			if (full == true) {
				cout << fixed << setprecision(2) << movieName << " - " << ((totalCapacity - freeSeats) / totalCapacity)*100 << "% full." << endl;
			}
		}
		else {
			cout << fixed << setprecision(2) << "Total tickets: " << totalTicketsSold << "\n" << (studentTickets / totalTicketsSold)*100 << "% student tickets.\n" << (standardTickets / totalTicketsSold)*100 << "% standard tickets.\n" << (kidsTickets / totalTicketsSold)*100 << "% kids tickets.";
			break;
		}
	}
}
