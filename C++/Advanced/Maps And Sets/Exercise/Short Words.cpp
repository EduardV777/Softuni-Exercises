#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	string text, currWord="";
	getline(cin,text);
	set<string> words;
	for(int k=0;k<=text.length();k++){
		if(text[k]==' ' || k==text.length()){
			transform(currWord.begin(),currWord.end(),currWord.begin(), ::tolower);
			if(currWord.length()<5){
				words.insert(currWord);
			}
			currWord="";
		}else {
			currWord+=text[k];	
		}
	}
	
	bool foundWords=false;
	for(string i: words){
		if(foundWords==true){
			cout<<", ";	
		}
		cout<<i;
		foundWords=true;
	}
	return 0;
}