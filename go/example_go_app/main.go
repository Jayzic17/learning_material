// All code belongs to a Package. The 'package' command tells Go what Package the code defined in this file belongs to
package main

// Anything specified in the 'import' command is also itself a Package
import "fmt"

func main() {
	var a = "This is a string" // In Go, you must ALWAYS use variables, otherwise it's a compile-time error. Go implicitly determines the variable type
	const b = 30
	var c string    // Lets you explicitly define the type instead of what Go implies it to be
	d := "Gorczyca" // This type of declaration doesn't work w/ 'const' variables, and you're also not allowed to explicitly define the type

	c = "Jonathan"

	fmt.Println("Start of console output:")
	fmt.Printf("This is a string %v and this is a constant %v \n", a, b)
	fmt.Print("This is my name:" + c + d + "\n")

}
