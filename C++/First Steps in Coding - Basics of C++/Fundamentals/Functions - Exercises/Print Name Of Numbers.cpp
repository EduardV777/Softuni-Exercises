#include <iostream>
#include <string>
using namespace std;

void figureOutNum(string numSize, int unit, int tenths, int thousands = 0, int hundreds = 0) {
	int k;
	bool tenthsEqualOne = false;
	if (numSize == "unit") {
		k = 1;
	}
	if (numSize == "ten") {
		k = 2;
	}
	else if (numSize == "hundred") {
		k = 3;
	}
	else if (numSize == "thousand") {
		k = 4;
	}
	while (k != 0) {
		int digit;
		if (k == 4) {
			digit = thousands;
		}
		else if (k == 3) {
			digit = hundreds;
		}
		else if (k == 2) {
			digit = tenths;
		}
		else if(k==1) {
			digit = unit;
		}
		switch (digit) {
		case 0:
			if(k==1 && numSize=="unit") {
				cout << "zero";
			}
			break;
		case 1:
			if (k == 4) {
				cout << "one thousand ";
			}
			else if (k == 3) {
				cout << "one hundred ";
			}
			else if (k == 2) {
				tenthsEqualOne = true;
				k--;
				continue;
			}
			else if (k == 1) {
				if (tenthsEqualOne) {
					cout << "eleven";
				}
				else {
					cout << "one";
				}	
			}
			break;
		case 2:
			if (k == 4) {
				cout << "two thousand ";
				break;
			}
			else if (k == 3) {
				cout << "two hundred ";
			}
			else if (k == 2) {
				cout << "twenty ";
			}
			else if (k==1) {
				if (tenthsEqualOne) {
					cout << "twelve";
				}
				else {
					cout << "two";
				}
			}
			break;
		case 3:
			if (k == 4) {
				cout << "three thousand ";
				break;
			}
			else if (k == 3) {
				cout << "three hundred ";
			}
			else if (k == 2) {
				cout << "thirty ";
			}
			else {
				if (tenthsEqualOne) {
					cout << "thirteen";
				}
				else {
					cout << "three";
				}
			}
			break;
		case 4:
			if (k == 4) {
				cout << "four thousand ";
				break;
			}
			else if (k == 3) {
				cout << "four hundred ";
			}
			else if (k == 2) {
				cout << "fourty ";
			}
			else if(k==1) {
				if (tenthsEqualOne) {
					cout << "fourteen";
				}
				else {
					cout << "four";
				}
			}
			break;
		case 5:
			if (k == 4) {
				cout << "five thousand ";
				break;
			}
			else if (k == 3) {
				cout << "five hundred ";
			}
			else if (k == 2) {
				cout << "fifty ";
			}
			else if(k==1) {
				if (tenthsEqualOne) {
					cout << "fifteen";
				}
				else {
					cout << "five";
				}
			}
			break;
		case 6:
			if (k == 4) {
				cout << "six thousand ";
				break;
			}
			else if (k == 3) {
				cout << "six hundred ";
			}
			else if (k == 2) {
				cout << "sixty ";
			}
			else if(k==1) {
				if (tenthsEqualOne) {
					cout << "sixteen";
				}
				else {
					cout << "six";
				}
			}
			break;
		case 7:
			if (k == 4) {
				cout << "seven thousand ";
				break;
			}
			else if (k == 3) {
				cout << "sevent hundred ";
			}
			else if (k == 2) {
				cout << "seventy ";
			}
			else if(k==1) {
				if (tenthsEqualOne) {
					cout << "seventeen";
				}
				else {
					cout << "seven";
				}
			}
			break;
		case 8:
			if (k == 4) {
				cout << "eight thousand ";
				break;
			}
			else if (k == 3) {
				cout << "eight hundred ";
			}
			else if (k == 2) {
				cout << "eighty ";
			}
			else if(k==1) {
				if (tenthsEqualOne) {
					cout << "eighteen";
				}
				else {
					cout << "eight";
				}
			}
			break;
		case 9:
			if (k == 4) {
				cout << "nine thousand ";
				break;
			}
			else if (k == 3) {
				cout << "nine hundred ";
			}
			else if (k == 2) {
				cout << "ninety ";
			}
			else if(k==1) {
				if (tenthsEqualOne) {
					cout << "nineteen";
				}
				else {
					cout << "nine";
				}
				break;
			}
		}
		k--;
	}
}

int main() {
	int num;
	cin >> num;
	if (num >= 0 && num < 10) {
		int units = num;
		figureOutNum("unit", units, 0, 0, 0);
	}
	else if (num >=10 && num<100) {
		int tenths = num / 10;
		int units = num % 10;
		figureOutNum("ten", units, tenths);
	}
	else if (num >= 100 && num < 1000) {
		int hundreds = num / 100;
		int tenths = (num-hundreds*100) / 10;
		if (tenths >= 10) {
			tenths /= 10;
		}
		int units = num % 10;
		figureOutNum("hundred", units, tenths, 0, hundreds);
	}
	else if (num >= 1000 && num <= 9999) {
		int thousands = num / 1000;
		int hundreds = (num - thousands * 1000) / 100;
		int tenths = (num - (thousands * 1000)-(hundreds*100))/10;
		if (tenths >= 10) {
			tenths /= 10;
		}
		int units = num % 10;
		figureOutNum("thousand", units, tenths, thousands, hundreds);
	}
	return 0;
}
