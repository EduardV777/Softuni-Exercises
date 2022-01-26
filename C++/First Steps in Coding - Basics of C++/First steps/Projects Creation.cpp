#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	string architect_name; int projects, required_time;
 	cin>>architect_name; cin>>projects;
    required_time=projects*3;
  	cout<<"The architect "<<architect_name<<" will need "<<required_time<<" hours to complete "<<projects<<" project/s.";
  return 0;
}