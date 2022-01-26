#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	string FirstName, LastName, town; int age;
  	cin>>FirstName; cin>>LastName; cin>>age; cin>>town;
  	cout<<"You are "<<FirstName<<" "<<LastName<<", a "<<age<<"-years old person from "<<town<<".";
  return 0;
}