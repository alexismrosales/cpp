package main

import (
	"fmt"
	"math"
)

func main() {
	basic()
	forLoop()
	ifStatement()
	arrays()
	mapStructure()
	println(randonfun(5, 10))

	// Recieve multiple return values
	a, b := mvalues()
	print("returning an int:", a, ", returning a string ", b)

	minput("string0...", "string1...", "string2...", "string3...")

	// Getting the anonymus function
	function1 := closurefunc(0)
	function2 := closurefunc(1)
	// Invoking the funcitions
	println("if 0", function1(), "if 1", function2())
}

func basic() {
	// Variables With types
	var a, b int = 0, 1
	fmt.Println("a =", a, "b =", b) // Printing using fmt
	fmt.Printf("a = %d b = %d\n", a, b)
	// Withot types
	c, d := 2, 3 // this is equal to var c,d = 2 ,3
	fmt.Println("c =", c, "d =", d)
	// Constants (has no type until is used)
	const myconst = 500000000
	println(3e20 / myconst) // Print take the const as an int
	// Convert to type string
	println(int(3e20 / myconst)) // Printing without declare fmt
	println(math.Sin(myconst))
}

func forLoop() {
	// For loops is not necesary all common args
	i := 20
	for i <= 30 {
		fmt.Println("Actual value:", i)
		i += 5
	}

	for i := 0; i < 3; i++ {
		fmt.Println("helloworld")
	}

	for i := range 6 {
		if i%2 != 0 {
			continue // It jumps to the next loop
		}
		println("val: ", i)
	}
}

func ifStatement() {
	// You can also declare ONE variable into the ifStatement
	if i := 5; i <= 6 {
		println(i)
	}
}

func arrays() {
	arr := [5]int{1, 2, 3, 4, 5}

	fmt.Println(arr) // To print the full list you need fmt
	for i := range 5 {
		println(arr[i])
	}
}

func mapStructure() {
	mp := make(map[string]int) // "map[Key type]valueType"
	mp["key1"] = 4
	mp["key2"] = -4
	println("map val", mp["key1"])
	delete(mp, "key1")
	fmt.Println(mp)
}

// Functions (parameters) return type
func randonfun(a, b int) int {
	return a + b
}

// Return multiple values
func mvalues() (int, string) {
	return 100, "second value"
}

// Variadic functions: Multiple inputs for Functions
func minput(inputs ...string) {
	for index, input := range inputs {
		println("\n", index, ": ", input)
	}
}

// Closure functions //You can return anonymus functions
func closurefunc(input int) func() string {
	if input == 0 {
		return func() string {
			str1, str2 := "hola", "mundo"
			return str1 + " " + str2
		}
	}
	return func() string {
		str1, str2 := "adios", "universo"
		return str1 + " " + str2
	}
}
