#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	double trainingYearlyFee, basketShoesPrice, basketClothesPrice, basketBallPrice, basketAccesoriesPrice, cost;
	cin >> trainingYearlyFee;
	basketShoesPrice = trainingYearlyFee-trainingYearlyFee * 0.4; basketClothesPrice = basketShoesPrice - (basketShoesPrice * 0.2); basketBallPrice = basketClothesPrice / 4; basketAccesoriesPrice = basketBallPrice / 5;
	cost = basketShoesPrice + basketClothesPrice + basketBallPrice + basketAccesoriesPrice + trainingYearlyFee;
	cout << cost;
}