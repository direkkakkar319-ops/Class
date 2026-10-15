package main

import "fmt"

// var jwtToken := 30000 not allowed
const LoginToken string = "svdsfewfewew"

func main()  {
	var username string = "Direk"
	fmt.Println("Name: ", username)
	fmt.Printf("Variable is of type: %T \n", username)

	var isLoggedIn bool = true
	fmt.Println("Login status: ", isLoggedIn)
	fmt.Printf("Variable is of type: %T \n", isLoggedIn)
	
	var smallVal  uint8 = 255
	fmt.Println(smallVal)
	fmt.Printf("Variable is of type: %T \n", smallVal)
	
	var smallFloat float32 = 255.33435325342632523525
	fmt.Println(smallFloat)
	fmt.Printf("Variable is of type: %T \n", smallFloat)
	
	var normalFloat float64 = 255.33435325342632523525
	fmt.Println(normalFloat)
	fmt.Printf("Variable is of type: %T \n", normalFloat)

	// default values and some aliases
	var anotherVariable int
	fmt.Println(anotherVariable)
	fmt.Printf("Variable is of type: %T \n", anotherVariable)

	// implicit type
	var website = "hell.in"
	fmt.Println(website)
	fmt.Printf("Variable is of type: %T \n", website)

	// no var style
	numberOfUsers := 3000000
	fmt.Println(numberOfUsers)
}
