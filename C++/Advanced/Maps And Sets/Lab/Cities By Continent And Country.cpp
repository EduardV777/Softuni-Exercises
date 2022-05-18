#include <iostream>
#include <map>
#include <utility>
#include <string>
using namespace std;

int main() {
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
			map<string, string> locations;
			places[continent] = locations;

		}
		map<string, string>& mapLink = places[continent];
		auto find2 = mapLink.find(country);
		if (find2 == mapLink.end()) {
			mapLink[country] = "";
		}
		if (mapLink[country].length() > 0) {
			mapLink[country] += ", ";
		}
		mapLink[country] += city;
		n--;
	}

	for (auto c = places.begin(); c != places.end(); c++) {
		map<string, string>& mapLink = c->second;

		cout << c->first << ": \n";
		for (auto c2 = mapLink.begin(); c2 != mapLink.end(); c2++) {
			cout << "	" << c2->first << " -> " << c2->second << endl;
		}
	}
	return 0;
}