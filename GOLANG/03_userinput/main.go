package main

import "fmt"
import "bufio"
import "os"

func main(){
	welcome := "Welcome to the User Input Program!"
	fmt.Println(welcome)
	
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Please enter rating for the order: ")
	
	// comma ok || error ok
	input, err := reader.ReadString('\n') 
	if err != nil {
		fmt.Println("Error reading input:", err)
		return
	}
	
	fmt.Println("Thank you for your rating!")
	fmt.Println("You entered:", input)
	fmt.Printf("Type of input is %T", input)
}
