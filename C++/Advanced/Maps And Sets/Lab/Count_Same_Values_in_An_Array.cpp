#include <iostream>
#include <map>

using namespace std;


int main() {
	string numbers, num="";
	double* values=new double [100];
	int j=0;
	getline(cin>>ws,numbers);
	map<double,double> numbersCounter;
	for(int k=0;k<=numbers.length();k++){
		if(numbers[k]==' ' || k==numbers.length()){
			double currNum=stod(num);
			auto res=numbersCounter.find(currNum);
			if(res==numbersCounter.end()){
				numbersCounter[currNum]=1;
				values[j]=currNum;
				j++;
			}else {
				numbersCounter[currNum]+=1;	
			}
			num="";
		}else {
			num+=numbers[k];	
		}
	}
	
	for(int k=0;k<j;k++){
		auto res=numbersCounter.find(values[k]);
		cout<<res->first<<" - "<<res->second<<" times"<<endl;
	}
	return 0;
}