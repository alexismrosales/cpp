package main

import (
	"math"
	"strconv"
)

func isHappy(n int) bool {
	visitedM := make(map[int]struct{})
	for {
		if _, visited := visitedM[n]; visited {
			break
		}
		if n == 1 {
			return true
		}
		sum := 0
		digits := getDigits(n)
		for i := 0; i < len(digits); i++ {
			digits[i] = int(math.Pow(float64(digits[i]), 2))
			sum += digits[i]
		}
		visitedM[n] = struct{}{}
		n = sum
	}
	return false
}

func getDigits(n int) []int {
	sN := strconv.Itoa(n)
	digits := make([]int, len(sN))
	for i := 0; i < len(sN); i++ {
		digits[i] = getDigit(n, len(sN)-i)
	}
	return digits
}

func getDigit(num, place int) int {
	r := num % int(math.Pow(10, float64(place)))
	return r / int(math.Pow(10, float64(place-1)))
}
