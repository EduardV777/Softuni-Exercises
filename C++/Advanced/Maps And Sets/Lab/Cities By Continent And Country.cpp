#include <iostream>
#include <map>
#include <utility>
#include <string>
#include <vector>

using namespace std;

int main() {
	vector<string> continentsOrder, countriesOrder;
	map<string, map<string, string>> places;
	int n;
	cin >> n;
	while (n != 0) {
		//continent country city
		string data, continent, country, city, val = "";
		getline(cin >> ws, data);
		for (int k = 0; k <= data.length(); k++) {
			if (data[k] == ' ' || k == data.length()) {
				if (continent == "") {
					continent = val;
				}
				else if (country == "") {
					country = val;
				}
				else {
					city = val;
				}
				val = "";
			}
			else {
				val += data[k];
			}
		}
		auto find = places.find(continent);
		if (find == places.end()) {
			continentsOrder.push_back(continent);
			map<string, string> locations;
			places[continent] = locations;

		}
		map<string, string>& mapLink = places[continent];
		auto find2 = mapLink.find(country);
		if (find2 == mapLink.end()) {
			countriesOrder.push_back(country);
			mapLink[country] = "";
		}
		if (mapLink[country].length() > 0) {
			mapLink[country] += ", ";
		}
		mapLink[country] += city;
		n--;
	}

	for (string c : continentsOrder) {
		auto continent = places.find(c);
		cout << continent->first << ":\n";

		for (string c2 : countriesOrder) {
			auto country = places[continent->first].find(c2);
			if (country != places[continent->first].end()) {
				cout << "  " << country->first << " -> " << country->second << endl;
			}
			else {
				continue;
			}
		}

	}
	return 0;
}