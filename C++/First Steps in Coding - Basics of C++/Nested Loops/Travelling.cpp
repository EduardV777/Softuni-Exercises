#include <iostream>
#include <string>
using namespace std;
int main() {
	double budget = 0;
	while (true) {
		string destination;
		getline(cin>>ws, destination);
		if (destination != "End") {
			double minBudget;
			cin >> minBudget;
			while (budget < minBudget) {
				double sum;
				cin >> sum;
				budget += sum;
			}
			cout << "Going to " << destination << "!" << endl;
			budget = 0;
		}
		else {
			break;
		}
	}
}
