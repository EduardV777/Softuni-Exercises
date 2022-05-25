#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
	string numbers, currNum="";
	getline(cin,numbers);
	set<int, greater<int>> numbersSet;
	for(int k=0;k<=numbers.length();k++){
		if(numbers[k]==' ' || k==numbers.length()){
			bool square=false;
			int num=stoi(currNum);
			for(int div=1;div<=10;div++){
				if(div*div==num){
					square=true;	
				}
			}
			if(square==true){
				numbersSet.insert(num);
			}
			currNum="";
		}else {
			currNum+=numbers[k];	
		}
	}
	cout<<endl;
	for(int i: numbersSet){
		cout<<i<<" ";	
	}
	return 0;
}