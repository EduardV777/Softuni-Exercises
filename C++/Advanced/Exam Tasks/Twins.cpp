#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;


int main() {
	map<string, vector<string>> customers = { pair<string, vector<string>>("Mimi", {}), pair<string, vector<string>>("Pepi", {}) };
	int n;
	cin >> n;

	while (n != 0) {
		string line, cashier, customer, minutes, currVal;
		int i = 0;
		getline(cin >> ws, line);

		for (int k = 0; k <= line.length(); k++) {
			if (k == line.length() || line[k] == ' ') {
				if (i == 0) {
					cashier = currVal;
				}
				else if (i == 1) {
					customer = currVal;
				}
				else {
					minutes = currVal;
				}
				currVal = "";
				i++;
			}
			else {
				currVal += line[k];
			}
		}

		customers[cashier].push_back(customer);
		customers[cashier].push_back(minutes);
		n--;
	}

	int minutesToRecord;
	cin >> minutesToRecord;

	while (minutesToRecord > 0) {
		//pepi turn
		if (customers["Pepi"].empty()) {
			cout << "Pepi Idle\n";
		}
		else {
			cout << "Pepi processing " << customers["Pepi"][0] << endl;
			int customerMinutes = stoi(customers["Pepi"][1]);
			customerMinutes--;
			customers["Pepi"][1] = to_string(customerMinutes);
			if (customers["Pepi"][1] == "0") {
				customers["Pepi"].erase(customers["Pepi"].begin() + 1);
				customers["Pepi"].erase(customers["Pepi"].begin());
			}
		}
		//mimi turn
		if (customers["Mimi"].empty()) {
			cout << "Mimi Idle\n";
		}
		else {
			cout << "Mimi processing " << customers["Mimi"][0] << endl;
			int customerMinutes = stoi(customers["Mimi"][1]);
			customerMinutes--;
			customers["Mimi"][1] = to_string(customerMinutes);
			if (customers["Mimi"][1] == "0") {
				customers["Mimi"].erase(customers["Mimi"].begin() + 1);
				customers["Mimi"].erase(customers["Mimi"].begin());
			}	
		}
		minutesToRecord--;
	}

	return 0;
}