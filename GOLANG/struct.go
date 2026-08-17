package main
import "fmt"

type student struct{
	RollNo int
	Name string
	Marks float64
}

func main(){
	// var s student
	// s.Name = "Ayush"
	// s.RollNo = 45
	// s.Marks = 90

	// fmt.Print("Student Name")
	// fmt.Println(s.Name)
	// fmt.Print("Roll No")
	// fmt.Println(s.RollNo)
	// fmt.Print("Marks")
	// fmt.Println(s.Marks)

	// student2 := student{
	// 	Name : "RohanJ",
	// 	RollNo : 45,
	// 	Marks : 90,
	// }
	// fmt.Print("Student Name")
	// fmt.Println(student2.Name)
	// fmt.Print("Roll No")
	// fmt.Println(student2.RollNo)
	// fmt.Print("Marks")
	// fmt.Println(student2.Marks)
	// MovieInformation()
	LaptopConfiguration()
}

// type MovieInfo struct{
// 	Director, Title string
// 	ReleaseYear int 
// 	Rating float64
// }
// func MovieInformation(){
// 	m1 := MovieInfo{
// 		Title: "RRR",
// 		Director: "Rahul Kumar Shetty",
// 		ReleaseYear: 2025,
// 		Rating: 4.5,
// 	}
// 	fmt.Println(m1)
// }

type Laptop struct{
	Brand ,Processer string
	RAMInGB, StorageInGB int
}
func LaptopConfiguration(){
	features:=Laptop{
		Brand: "Dell",
		Processer: "Core i5",
		RAMInGB: 8,
		StorageInGB: 512,
	}
	fmt.Println(features)
	fmt.Println("Updated RAM")
	features.RAMInGB = 16
	fmt.Println(features)
}
 
