#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;
int main() {
    int dogs, misc_animals; double total, dog_foodPrice, misc_animals_foodPrice;
    cin >> dogs; cin >> misc_animals;
    dog_foodPrice = dogs * 2.50; misc_animals_foodPrice = misc_animals * 4;
    total = dog_foodPrice + misc_animals_foodPrice;
    cout <<fixed<<setprecision(2)<< total << " lv.";
    return 0;
}