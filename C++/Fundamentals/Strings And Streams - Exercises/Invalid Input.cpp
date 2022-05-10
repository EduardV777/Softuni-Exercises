#include <iostream>
#include <string>
using namespace std;

string* FindWords(string numbers) {
	string* wordsArr = new string[50], word="";
	int i = 0;
	bool wordFound = false;
	for (int k = 0; k < numbers.length(); k++) {
		if ((numbers[k] >= 'a' && numbers[k] <= 'z') || (numbers[k] >= 'A' && numbers[k] <= 'Z')) {
			word += numbers[k];
			wordFound = true;
		}
		else {
			if (wordFound == true) {
				wordsArr[i] = word;
				word = "";
				i++;
				wordFound = false;
			}
		}
	}
	if (wordFound == true) {
		wordsArr[i] = word;
		word = "";
		i++;
	}
	wordsArr[i] = "stop777";
	return wordsArr;
}

int CalculateSum(string numbers) {
	int sum = 0;
	string num = "";
	for (int k = 0; k < numbers.length(); k ++ ) {
		if (numbers[k] >= '0' && numbers[k] <= '9') {
			if (k>0 && numbers[k - 1] == '-') {
				num += "-";
			}
			num += numbers[k];
		}
		else {
			if (num.length() > 0) {
				sum += stoi(num);
				num = "";
			}
		}
	}
	if (num.length() > 0) {
		sum += stoi(num);
	}
	return sum;
}

int main() {
	string numbers, *words;
	getline(cin, numbers);
	int sumOfNums = CalculateSum(numbers);
	cout << sumOfNums << endl;
	words = FindWords(numbers);
	for (int k = 0; k < 50; k++) {
		if (words[k] == "stop777") {
			break;
		}
		cout << words[k] << " ";
	}
	return 0;
}
