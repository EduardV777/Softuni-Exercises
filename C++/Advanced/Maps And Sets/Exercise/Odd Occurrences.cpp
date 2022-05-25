#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	string words="", currWord="";
	getline(cin,words);
	vector<string> wordOrder;
	map<string,int> wordOccurrences;
	
	for(int k=0;k<=words.length();k++){
		if(words[k]==' ' || k==words.length()){
			bool existsInWordOrder=false;
			transform(currWord.begin(), currWord.end(), currWord.begin(), ::tolower);
			for(int vec=0;vec<wordOrder.size();vec++){
					if(currWord==wordOrder[vec]){
						existsInWordOrder=true;
					}
			}
			if(existsInWordOrder==false){
				wordOrder.push_back(currWord);
			}
			auto exists=wordOccurrences.find(currWord);
			if(exists==wordOccurrences.end()){
				wordOccurrences.insert(pair<string,int>{currWord, 1});
			}else {
				wordOccurrences[currWord]+=1;
			}
			currWord="";
		}else{
			currWord+=words[k];
		}
	}
	bool foundValues=false;
	for(int vec=0;vec<wordOrder.size();vec++){
		auto find=wordOccurrences.find(wordOrder[vec]);
		if(find->second%2!=0){
			if(foundValues==true){
				cout<<", ";
			}
			cout<<find->first;
			foundValues=true;
		}
	}
	return 0;
}