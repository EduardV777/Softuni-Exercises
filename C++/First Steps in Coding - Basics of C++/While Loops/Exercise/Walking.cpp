#include <iostream>
#include <string>
using namespace std;

int main() {
	int stepsGoal = 10000, totalSteps=0;
	bool goalReached = false;
	while (true) {
		string steps;
		getline(cin, steps);
		if (steps != "Going home") {
			int stepsDone = stoi(steps);
			totalSteps += stepsDone;
			if (totalSteps >= stepsGoal) {
				goalReached = true;
				break;
			}
		}
		else {
			int stepsOnWayHome;
			cin >> stepsOnWayHome;
			totalSteps += stepsOnWayHome;
			if (totalSteps >= stepsGoal) {
				goalReached = true;
				break;
			}
			else {
				break;
			}
		}
	}

	if (goalReached == false) {
		cout << stepsGoal - totalSteps << " more steps to reach goal.";
	}
	else {
		cout << "Goal reached! Good job!";
	}
}
