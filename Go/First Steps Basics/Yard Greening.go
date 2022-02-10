package main

import "fmt"

func main() {
	var qMeters, pricePerMeter, expense, discount float32
	pricePerMeter = 7.61
	fmt.Scanln(&qMeters)
	expense = qMeters * pricePerMeter
	discount = expense * 0.18
	expense -= discount
	output := fmt.Sprintf("The final price is: %f lv.\nThe discount is: %f lv.", expense, discount)
	fmt.Println(output)
}
