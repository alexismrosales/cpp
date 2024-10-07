package main

import (
	"strings"
	"unicode"
)

func isPalindrome(s string) bool {
	// Clearing the string
	alphanumericS := strings.Map(toAlphanumeric, s)
	// Two pointers
	m, n := 0, len(alphanumericS)-1
	// Iteraring over the half of the size of characters of the string
	for m < n {
		if alphanumericS[m] != alphanumericS[n] {
			return false
		}
		m++
		n--
	}
	return true
}

// toAlphanumeric(r) -- Check if a alphanumeric number is valid
func toAlphanumeric(r rune) rune {
	if !unicode.IsLetter(r) || !unicode.IsDigit(r) {
		return -1
	}
	return unicode.ToLower(r)
}
