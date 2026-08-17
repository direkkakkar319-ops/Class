package main
import (
	"fmt"
	"sync"
)

var counter int
var mu      sync.Mutex
var wg      sync.WaitGroup

func main() {
	wg.Add(2)
	go Increment()
	go Increment()
	wg.Wait()
	fmt.Println(counter)

	fmt.Println()

	wg.Add(1)
	go greet()
	wg.Wait()
	fmt.Println("greetings ended")

	fmt.Println()

	wg.Add(2)
	go download()
	go process()
	wg.Wait()
	fmt.Println("Ended")

	fmt.Println()

	Read()
	Write()
	Read()

	fmt.Println()

	wg.Add(3)
	Hello()
	Welcome()
	GoodMorning()
	wg.Wait()
	fmt.Println(messages)
}

func Increment() {
	defer wg.Done()
	for i := 0; i < 1000; i++ {
		mu.Lock()
		counter++
		mu.Unlock()
	}
}

func greet(){
	defer wg.Done()
	fmt.Println("Hello From Goroutine")
}

func download(){
	defer wg.Done()
	fmt.Println("Downloading File")
}

func process(){
	defer wg.Done()
	fmt.Println("Processing Data")
}

var number = 100
var rw sync.RWMutex

func Read(){
	rw.RLock()
	fmt.Println(number)
	rw.RUnlock()
}

func Write(){
	rw.Lock()
	number++
	rw.Unlock()
}

var messages []string

func Hello(){
	defer wg.Done()
	messages = append(messages, "Hello")
}

func Welcome(){
	defer wg.Done()
	messages = append(messages, "Welcome")
}

func GoodMorning(){
	defer wg.Done()
	messages = append(messages, "Good Morning")
}
