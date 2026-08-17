package main
import "fmt"

func main(){
	// employee()
	// rectangle()
	// bill()
	// gross_salary()
	// percentage_calculator()
	// books()
	// hotel_bill()
	scholarship()
}

// func employee(){
// 	Employee_name := "Employee"
// 	Employee_ID := 101
// 	Department := 1999
// 	fmt.Println("EMPLOYEE NAME")
// 	fmt.Println(Employee_name)
// 	fmt.Println("EMPLOYEE ID")
// 	fmt.Println(Employee_ID)
// 	fmt.Println("EMPLOYEE DEPARTMENT")
// 	fmt.Println(Department) 
// }

// func rectangle(){
// 	length := 10
// 	width := 5
// 	area := length * width
// 	perimeter := 2*(length + width)
// 	fmt.Println("AREA OF RECTANGLE")
// 	fmt.Println(area)
// 	fmt.Println("PERIMETER OF RECTANGLE")
// 	fmt.Println(perimeter)
// }

// func bill(){
// 	fmt.Println("BILL CALCULATOR")
// 	var product_one float64
// 	var product_two float64
// 	var product_three float64
	
// 	fmt.Println("Enter price of product 1, 2, 3")
// 	fmt.Scan(&product_one, &product_two, &product_three)

// 	total_bill := product_one + product_two + product_three
// 	fmt.Println("TOTAL BILL")
// 	fmt.Println(total_bill)

// 	fmt.Println("GST")
// 	gst := 0.18 * total_bill
// 	fmt.Println(gst)

// 	final_bill := total_bill + gst
// 	fmt.Println("FINAL BILL")
// 	fmt.Println(final_bill)
// }

// func gross_salary(){
// 	fmt.Println("GROSS SALARY CALCULATOR")
// 	var basic_salary float64

// 	fmt.Println("Enter basic salary")
// 	fmt.Scan(&basic_salary)
	
// 	house_rent_allowance := 0.2 * basic_salary
// 	fmt.Println("HOUSE RENT ALLOWANCE")
// 	fmt.Println(house_rent_allowance)

// 	dearness_allowance := 0.10 * basic_salary
// 	fmt.Println("DEARNESS ALLOWANCE")
// 	fmt.Println(dearness_allowance)
// }

// func percentage_calculator(){
// 	var student_name string
// 	var sub_one int 
// 	var sub_two int 
// 	var sub_three int 
// 	var sub_four int 
// 	var sub_five int 
// 	var total_marks float64
// 	var percentage float64

// 	fmt.Print("Enter name")
// 	fmt.Scan(&student_name)

// 	fmt.Print("Enter marks in five subjects")
// 	fmt.Scan(&sub_one, &sub_two, &sub_three, &sub_four, &sub_five)
	
// 	total_marks = float64(sub_one + sub_two + sub_three + sub_four + sub_five)

// 	percentage = (total_marks / 500) * 100

// 	fmt.Println("RESULT")
// 	fmt.Print("SUBJECTS")
// 	fmt.Println(sub_one ,sub_two, sub_three, sub_four ,sub_five)
	
// 	fmt.Print("TOTAL MARKS")
// 	fmt.Println(total_marks)
	
// 	fmt.Println("PERCENTAGE")
// 	fmt.Println(percentage)
// }

// func books(){
// 	var book_name ,Author_Name string
// 	var book_price ,copies int
// 	var total_price float64

// 	fmt.Println("Enter the book name")
// 	fmt.Scan(&book_name)

// 	fmt.Println("Enter the author name")
// 	fmt.Scan(&Author_Name)
	
// 	fmt.Println("Enter the price of book")
// 	fmt.Scan(&book_price)
	
// 	fmt.Println("Enter the number of copies")
// 	fmt.Scan(&copies)
	
// 	total_price = float64(book_price * copies)
	
// 	fmt.Print("Total Price")
// 	fmt.Println(total_price)
// }

// func hotel_bill(){
// 	var Customer_Name, Room_Incharge string
// 	var Food_Bill, Laundry_Charge int
// 	var Total_Bill , gst_charge , Final_Amount float64
// 	fmt.Print("Enter Customer Name")
// 	fmt.Scan(&Customer_Name)

// 	fmt.Print("Enter Room Incharge")
// 	fmt.Scan(&Room_Incharge)

// 	fmt.Print("Enter Food Bill")
// 	fmt.Scan(&Food_Bill)
	
	// fmt.Print("Enter Laundry Bill")
	// fmt.Scan(&Laundry_Charge)

	// Total_Bill = float64(Food_Bill + Laundry_Charge)
	// gst_charge = 0.18 * Total_Bill
	// Final_Amount = Total_Bill + gst_charge

	// fmt.Print("Customer Name")
	// fmt.Println(Customer_Name)
	
	// fmt.Print("Room Incharge")
	// fmt.Println(Room_Incharge)
	
	// fmt.Print("Food Bill")
	// fmt.Println(Food_Bill)
	
// 	fmt.Print("Laundry Bill")
// 	fmt.Println(Laundry_Charge)
	
// 	fmt.Print("Total Bill")
// 	fmt.Println(Total_Bill)
	
// 	fmt.Print("GST Imposed 18%")
// 	fmt.Println(gst_charge)
	
// 	fmt.Print("Final Amount to be paid")
// 	fmt.Println(Final_Amount)
// }

func scholarship(){
	var percentage , attendence float64

	fmt.Print("Enter percentage scored")
	fmt.Scan(&percentage)

	fmt.Print("Enter Attendence")
	fmt.Scan(&attendence)

	if (percentage >= 95 && attendence >= 90){
		fmt.Println("100 percent scholarship awarded")
	} else if (percentage >= 90 && attendence >= 80){
		fmt.Println("75 percent scholarship awarded")
	} else if (percentage >=85 && attendence >= 75){
		fmt.Println("50 percent scholarship awarded")
	} else{
		fmt.Println("Scholarship will not we granted")
	}
}
