package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main(){
	fmt.Println("Welcome to our pizza application")
	fmt.Println("Please rate our pizza from 1 to 5")

	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	
	fmt.Println("Thanks for rating", input)
	
	numRating , err := strconv.ParseFloat(strings.TrimSpace(input), 64)
	fmt.Println("Your rating:", numRating)
	
	if err!=nil{
		fmt.Println(err)
	} else {
		fmt.Println("Added one to your rating", numRating+1)
	}
}
