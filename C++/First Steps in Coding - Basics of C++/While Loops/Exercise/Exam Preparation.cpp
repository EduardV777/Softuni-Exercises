#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
	int badGradesCount, badGrades=0, k=0;
	double gradesSum = 0;
	cin >> badGradesCount;
	string problemName, currProblem;
	while (true) {
		getline(cin>>ws, problemName);
		if (problemName != "Enough") {
			currProblem = problemName;
			k += 1;
			double grade;
			cin >> grade;
			gradesSum += grade;
			if (grade <= 4.00) {
				badGrades += 1;
			}
			if (badGrades == badGradesCount) {
				cout << "You need a break, " << badGrades << " poor grades.";
				break;
			}
		}
		else {
			double avgScore = (double)gradesSum / k;
			cout << fixed << setprecision(2) << "Average score: " << avgScore << "\nNumber of problems: " << k << "\nLast problem: " << currProblem;
			break;
		}
	}
}
