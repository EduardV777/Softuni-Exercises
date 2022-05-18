#include <iostream>
#include <map>
#include <utility>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	map<string, vector<double>> studentRecord;
	int n;
	cin >> n;
	while (n != 0) {
		string studentName, studentData, val = "";
		double grade;
		getline(cin >> ws, studentData);
		for (int k = 0; k <= studentData.length(); k++) {
			if (studentData[k] == ' ' || k == studentData.length()) {
				if (studentName == "") {
					studentName = val;
				}
				else {
					grade = stod(val);
				}
				val = "";
			}
			else {
				val += studentData[k];
			}
		}
		auto check = studentRecord.find(studentName);
		if (check == studentRecord.end()) {
			vector<double> grades{ grade };
			studentRecord.insert(pair<string, vector<double>>{studentName, grades});
		}
		else {
			studentRecord[studentName].push_back(grade);
		}
		n--;
	}
	cout << endl << endl;

	for (auto k : studentRecord) {
		double sumGrades = 0;
		cout << fixed << setprecision(2) << k.first << " -> ";
		vector<double>vectorLink = k.second;
		for (int j = 0; j < vectorLink.size(); j++) {
			cout << vectorLink[j] << " ";
			sumGrades += vectorLink[j];
		}
		cout << "(avg: " << sumGrades / vectorLink.size() << ")\n";
	}
	return 0;
}