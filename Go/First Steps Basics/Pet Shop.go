package main

import "fmt"

func main() {
	var packsDogFood, packsCatFood int
	var totalExpense, dogFoodPrice, catFoodPrice float32
	dogFoodPrice = 2.50
	catFoodPrice = 4.00
	fmt.Scanln(&packsDogFood)
	fmt.Scanln(&packsCatFood)
	totalExpense = (dogFoodPrice * float32(packsDogFood)) + (catFoodPrice * float32(packsCatFood))
	output := fmt.Sprintf("%v lv.", totalExpense)
	fmt.Println(output)
}
