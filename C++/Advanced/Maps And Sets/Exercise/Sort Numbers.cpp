#include <iostream>
#include <set>

using namespace std;


int main() {
	string numbers, currNum="";
	getline(cin,numbers);
	set<int> numbersSet;
	for(int k=0;k<=numbers.length();k++){
		if(numbers[k]==' ' || k==numbers.length()){
			numbersSet.insert(stoi(currNum));
			currNum="";
		}else {
			currNum+=numbers[k];	
		}
	}
	
	bool foundNumber=false;
	for(int i: numbersSet){
		if(foundNumber==true){
			cout<<" <= ";	
		}
		cout<<i;
		foundNumber=true;
	}
	return 0;
}