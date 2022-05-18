#include <iostream>
#include <map>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	map<string,vector<double>> studentsAvg;
	int k;
	cin>>k;
	while (k!=0){
		string studentData, val="", name;
		getline(cin>>ws, studentData);
		int nameOrGrade=0;
		for(int j=0;j<=studentData.length();j++){
			if(studentData[j]==' ' || j==studentData.length()){
				if (nameOrGrade==0){
					auto res=studentsAvg.find(val);
					if(res==studentsAvg.end()){
						studentsAvg[val]=vector<double> ();
					}
					name=val;
					nameOrGrade+=1;
				}else if(nameOrGrade==1){
					studentsAvg[name].push_back(stod(val));
				}
				val="";
			}else {
				val+=studentData[j];
			}
		}
		k--;
	}
	for(auto j=studentsAvg.begin();j!=studentsAvg.end();j++){
		double avgGrade=0;
		cout<<fixed<<setprecision(2)<<j->first<<" -> ";
		vector<double>vecLink=j->second;
		for(auto k=vecLink.begin();k!=vecLink.end();k++){
			cout<<*k<<" ";
			avgGrade+=*k;
		}
		avgGrade/=vecLink.size();
		cout<<"(avg: "<<avgGrade<<")\n";
	}
	
	return 0;
}