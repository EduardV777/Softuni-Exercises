#include <cstdlib>
#include <iostream>
#include <stack>
#include <climits>
using namespace std;

void findX(stack<int> &numbers, int x){
	int smallestVal=INT_MAX;
	bool foundX=false;
	while(true){
		if(numbers.empty()){
			break;
		}
		if(numbers.top()==x){
			cout << "true";
			foundX=true;
			break;
		} else {
			if(smallestVal>numbers.top()){
				smallestVal=numbers.top();
			}
			numbers.pop();
		}
	}
	if(foundX==false){
		cout<<smallestVal;
	}
  }

int main() {
	int n,s,x,k=0;
	bool foundX=false;
	cin>>n>>s>>x;
	stack<int> numbers;
	while(k<n){
		int num;
		cin>>num;
		numbers.push(num);
		k++;
	}
	k=0;
	while(k<s){
		numbers.pop();
		k++;
	}
	if(numbers.empty() || n==s){
		cout << "0";
	}else {
		findX(numbers,x);
	}
	return 0;
}