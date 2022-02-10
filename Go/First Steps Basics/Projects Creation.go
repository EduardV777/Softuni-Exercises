package main

import "fmt"

func main() {
	var archName string
	var projects, totalTime, timePerProject int
	timePerProject = 3
	fmt.Scanln(&archName)
	fmt.Scanln(&projects)
	totalTime = timePerProject * projects
	output := fmt.Sprintf("The architect %v will need %v hours to complete %v project/s.", archName, totalTime, projects)
	fmt.Println(output)
}
