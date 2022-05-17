#include <utility>
#include <iostream>

using namespace std;

int main() {
	std::pair<int, string> pairVar(35988000000, "Eduard Velkov");
	cout << "Pair variable values: \n"<<pairVar.first<<" - "<<pairVar.second<<"\n";
	return 0;
}