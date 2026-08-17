package main
import "fmt"

func main(){
	// salary()
	Duration()
}

// type employee struct{
// 	name string
// 	basicSalary ,bonus float64
// }
// func salary(){ 
// 	var e employee 
	
// 	fmt.Print("Enter Your name: ")
// 	fmt.Scan(&e.name)
	
// 	fmt.Print("Enter Basic Salary: ")
// 	fmt.Scan(&e.basicSalary)
	
// 	fmt.Print("Enter bonus amount: ")
// 	fmt.Scan(&e.bonus)

// 	finalSalary := e.basicSalary + e.bonus 
// 	fmt.Print("Final Salary is=")
// 	fmt.Println(finalSalary)
// }

type movie struct{
	title string
	hours, minutes float64
}
func Duration(){
	var m movie
	fmt.Print("Movie Name : ")
	fmt.Scan(&m.title)

	fmt.Print("Enter Number of Hours : ")
	fmt.Scan(&m.hours)

	fmt.Print("Enter Number of minutes : ")
	fmt.Scan(&m.minutes)

	totalMinutes := m.hours*60 + m.minutes
	fmt.Print("total minutes : ")
	fmt.Println(totalMinutes)
}

