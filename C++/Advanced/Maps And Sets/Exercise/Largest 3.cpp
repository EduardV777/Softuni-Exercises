#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

int main() {
	
	string numbers, currNum="";
	getline(cin,numbers);
	vector<int> numbersVec;
	set<int, greater<int>> numbersSet;
	for(int k=0;k<=numbers.length();k++){
		if(numbers[k]==' ' || k==numbers.length()){
			numbersVec.push_back(stoi(currNum));
			currNum="";
		}else {
			currNum+=numbers[k];
		}
	}
	
	
	for(int i=0;i<numbersVec.size()-1;i++){
		for(int j=0;j<numbersVec.size()-1;j++){
			if(numbersVec[j]>numbersVec[j+1]){
				int temp=numbersVec[j+1];
				numbersVec[j+1]=numbersVec[j];
				numbersVec[j]=temp;
			}
		}
	}
	
	int end=numbersVec.size()-4;
	if(numbersVec.size()<4){
		end=-1;	
	}
	for(int k=numbersVec.size()-1;k>end;k--){
		numbersSet.insert(numbersVec[k]);
	}

	for(int i: numbersSet){
		cout<<i<<" ";	
	}
	
	return 0;
}