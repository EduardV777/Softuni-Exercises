#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
	int n, presentations = 0;
	double totalGrade = 0;
	cin >> n;
	while (true) {
		double gradesSum=0, avgPresentGrade;
		string presentationName;
		getline(cin >> ws, presentationName);
		if (presentationName != "Finish") {
			presentations += 1;
			for (int k = 1; k <= n; k++) {
				double givenGrade;
				cin >> givenGrade;
				gradesSum += givenGrade;
			}
			avgPresentGrade = gradesSum / n;
			totalGrade += avgPresentGrade;
			cout << fixed << setprecision(2) << presentationName << " - " << avgPresentGrade << "." << endl;
		}
		else {
			double totalAvgGrade = totalGrade / presentations;
			cout << fixed << setprecision(2) << "Student's final assessment is " << totalAvgGrade << ".";
			break;
		}
	}

}
