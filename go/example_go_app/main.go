// All code belongs to a Package. The 'package' command tells Go what Package the code defined in this file belongs to
package main

// Anything specified in the 'import' command is also itself a Package
import "fmt"

var packageLevelVariable = 5 // This is how you define a variable at the Package level. You can't use the ":=" syntax when declaring variables here

func main() {
	var a = "This is a string" // In Go, you must ALWAYS use variables, otherwise it's a compile-time error. Go implicitly determines the variable type
	const b = 30
	var c string    // Lets you explicitly define the type instead of what Go implies it to be
	d := "Gorczyca" // This type of declaration doesn't work w/ 'const' variables, and you're also not allowed to explicitly define the type
	var e string
	fmt.Scan(&e)                              // Takes in user input and saves it at the address of variable e (&e is a pointer)
	var f = [6]string{"bob", "nancy", "drew"} // This is an Array. All array values need to be the same type. Not all values need to be defined on initialization
	var g = []string{}                        // This is a Slice (a.k.a ArrayLists)
	var h = true                              // This is a boolean
	var i = 5
	var j string
	var k int
	var l = make(map[string]string) // This is a Map, where "[string]" is the datatype for the keys, and "string" is the datatype for the values
	type UserData struct { // This is a Struct. Essentially a Class.
		firstName string   // The "type" keyword means this struct is effectively a new datatype
		lastName string
		email string
		id uint
		isCool bool
	}


	c = "Jonathan"
	f[3] = "sara"
	g = append(g, "Jon")
	j, k = introduceYourself("Andrew", 28)
	l["firstName"] = "Jonathan"
	var m = UserData { // This is an Object of our userData Struct. You don't have to set values for all the fields if you don't need to
		firstName: "Jonathan",
	}

	// This is a switch-case statement
	switch d {
	case "Gorczyca":
		fmt.Println(d)
	default:
		fmt.Println(d)
	}

	// This is an infinite loop
	/*for {

	}*/

	// This is a for-loop
	for index, value := range g {
		fmt.Println(g[index])
		f[4] = value
	}

	// This is also a for-loop. The "_" character means: "yes, iterate over this, but we won't be using it..."
	for _, value := range g {
		f[5] = value
	}

	// This is effectively a while-loop
	for i > 0 && h {
		h = false
		i -= 1
	}

	// This is an if-else statement
	if h && i == 5 {
		fmt.Println("h is true")
	} else if c == "Jonathan" {
		fmt.Println("c is Jonathan")
	} else {
		fmt.Println("h is false")
	}

	fmt.Println(packageLevelVariable)
	fmt.Println("Start of console output:")
	fmt.Printf("This is a string %v and this is a constant %v \n", a, b)
	fmt.Print("This is my name:" + c + d + "\n")
	fmt.Println(f[0])
	fmt.Printf("Array length: %v\n", len(f)) // Returns length of array
	fmt.Println(g)
	fmt.Println(sayHi("Jonathan"))
	fmt.Printf("%v %v\n", j, k)
	fmt.Println(l["firstName"])
	fmt.Println(m.firstName)
}

// This is a function. Make sure they're always declared at file scope like this (as opposed to within main() scope for example...)
func sayHi(name string) string {
	return "Hi, " + name
}

// This is a function that returns multiple values of different types
func introduceYourself(name string, age int) (string, int) {
	return "Hi, my name is: " + name + "and I am: ", age
}
