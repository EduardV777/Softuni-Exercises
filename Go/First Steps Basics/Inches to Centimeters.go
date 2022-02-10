package main

import "fmt"

func main() {
	var inches, centimeters float32
	fmt.Scanln(&inches)
	centimeters = inches * 2.54
	fmt.Print(centimeters)
}
