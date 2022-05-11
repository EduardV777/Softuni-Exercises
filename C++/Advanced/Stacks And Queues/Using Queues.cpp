#include <iostream>
#include <cstdlib>
#include <queue>
#include <string>
using namespace std;

void AddEvents(queue<string>& events, bool& stop) {
	string event;
	string command;
	cout << ">";
	getline(cin >> ws, command);
	cout << "\n";
	if (command == "add event") {
		while (true) {
			cout << "Enter event: ";
			getline(cin >> ws, event);
			if (event.length() > 0) {
				cout << "Process: [Adding event]\n";
				events.push(event);
				break;
			}
			else {
				cout << "\nError: Invalid event!\n";
				continue;
			}
		}
	}
	else if (command == "delete event") {
		if (events.size() > 0) {
			cout << "First event is - '" << events.front() << "'.\nAre you sure you wish to delete it?\n";
			string choice;
			getline(cin >> ws, choice);
			if (choice == "y" or choice == "yes") {
				cout << "\nProcess: [Deleting event " << events.front() << "]\n";
				events.pop();
			}
			else {
				cout << "Process: [Delete aborted]\n";
			}
		}
	}
	else if (command == "end") {
		stop = true;
	}
	else {
		cout << "\nInvalid command!\n";
	}
}

void outputQueueInfo(queue<string>& events) {
	int k = 1;
	while (events.size() > 0) {
		cout << "Event " << k << ": " << events.front() << ";\n";
		events.pop();
		k++;
	}
}

int main() {
	queue<string> events;
	bool stop = false;
	cout << "\n---Events journal---\n";
	while (true) {
		if (stop == true) {
			break;
		}
		AddEvents(events, stop);
	}
	outputQueueInfo(events);
	cout << "\nShutting down...\n";
	return 0;
}