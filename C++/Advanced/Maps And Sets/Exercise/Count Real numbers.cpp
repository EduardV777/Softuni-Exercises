#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
	string numbersList, currNum="";
	getline(cin, numbersList);
	map<double,int> numbers;
	for(int k=0;k<=numbersList.length();k++){
		if(numbersList[k]==' ' || k==numbersList.length()){
			double num=stod(currNum);
			auto exists=numbers.find(num);
			if(exists==numbers.end()){
				numbers.insert(pair<double,int>{num,1});
			}else {
				numbers[num]+=1;	
			}
			currNum="";
		}else{
			currNum+=numbersList[k];
		}
	}
	cout<<endl<<endl;
	for(auto i=numbers.begin();i!=numbers.end();i++){
		cout<<i->first<<" -> "<<i->second<<endl;
	}
	return 0;
}