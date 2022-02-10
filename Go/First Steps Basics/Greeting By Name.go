package main

import "fmt"

func main() {
	var name string
	fmt.Scanln(&name)
	message := fmt.Sprintf("Hello, %v!", name)
	fmt.Print(message)
}
