#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main() {
	map<string, vector<int>> cityTemperatures;
	int nCities;
	cin >> nCities;

	while (nCities != 0) {
		string city;
		int lowTemp, highTemp;
		getline(cin >> ws, city);
		cin >> lowTemp >> highTemp;

		auto cityExists = cityTemperatures.find(city);

		if (cityExists == cityTemperatures.end()) {
			cityTemperatures.insert(pair<string, vector<int>>(city, { lowTemp, highTemp }));
			nCities--;
		}
		else {
			if (lowTemp < cityTemperatures[city][0] && lowTemp < cityTemperatures[city][1]) {
				cityTemperatures[city][0] = lowTemp;
			}
			if (highTemp > cityTemperatures[city][1] && highTemp > cityTemperatures[city][0]) {
				cityTemperatures[city][1] = highTemp;
			}
		}
	}

	for (auto currCity = cityTemperatures.begin(); currCity != cityTemperatures.end(); currCity++) {
		cout << currCity->first << " " << currCity->second[0] << " " << currCity->second[1] << endl;
	}


	return 0;
}