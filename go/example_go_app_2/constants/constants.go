// If you have multiple main.go's in your repo where you want all of them to share the same variables,
// you can import them as a package to each main.go where the main.go's and the package to import
// have the file structure shown
package constants

const (

	// VERY IMPORTANT: Go uses the capitilization of the names of variables to determine variable scope,
	// so since this package is defined outside the main.go's it must be Upper Camel Case as shown.
	// If the variable is written in Camel Case, then it's only visible in the package where it's defined.
	ExampleGlobalVariable = "hello"
)
