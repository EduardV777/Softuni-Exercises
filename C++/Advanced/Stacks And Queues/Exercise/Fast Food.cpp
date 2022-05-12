#include <iostream>
#include <cstdlib>
#include <queue>
#include <string>
#include <climits>
using namespace std;

void loadOrders(queue<int>& orderList, string ordersString) {
	string numRepresent = "";
	for (int k = 0; k <= ordersString.length(); k++) {
		if (ordersString[k] == ' ' || k == ordersString.length()) {
			orderList.push(stoi(numRepresent));
			numRepresent = "";
			continue;
		}
		else {
			numRepresent += ordersString[k];
		}
	}
	queue<int> listCopy = orderList;
	int biggestOrder = INT_MIN;
	while (listCopy.size() != 0) {
		if (biggestOrder < listCopy.front()) {
			biggestOrder = listCopy.front();
		}
		listCopy.pop();
	}
	cout << biggestOrder << "\n";
}

void ServeClients(queue<int>& orderList, int food) {
	while (food > 0) {
		if (orderList.size() == 0) {
			break;
		}
		if (food >= orderList.front()) {
			food -= orderList.front();
			orderList.pop();
		}
		else {
			break;
		}
	}
	if (orderList.size() == 0) {
		cout << "Orders complete";
	}
	else {
		cout << "Orders left: ";
		while (!orderList.empty()) {
			cout << orderList.front() << " ";
			orderList.pop();
		}
	}

}

int main() {
	queue<int> orders;
	int qtyFood;
	string ordersString;
	cin >> qtyFood;
	getline(cin >> ws, ordersString);
	loadOrders(orders, ordersString);
	ServeClients(orders, qtyFood);
	return 0;
}