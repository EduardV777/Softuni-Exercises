#include <iostream>
#include <cstdlib>
#include <iomanip>
using namespace std;
int main() {
  double square_meters, total, costPerSquareMeter=7.61, sale;
  cin>>square_meters;
  total=(square_meters*costPerSquareMeter);
  sale=total*0.18;
  //Taking away the sale rate from total cost
  total-=sale;
  cout<<"The final price is: "<<fixed<<setprecision(2)<<total<<" lv.\nThe discount is: "<<sale<<" lv.";
  return 0;
}