package main

import "fmt"

func main() {
	var name, lastName, town string
	var age int
	fmt.Scanln(&name)
	fmt.Scanln(&lastName)
	fmt.Scanln(&age)
	fmt.Scanln(&town)
	message := fmt.Sprintf("You are %v %v, a %v-years old person from %v.", name, lastName, age, town)
	fmt.Print(message)
}
