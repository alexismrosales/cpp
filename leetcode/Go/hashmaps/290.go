package main

import "fmt"

func wordPattern(pattern string, s string) bool {
	strs := getWords(s)
	// In case we get different lengths
	if len(pattern) != len(strs) {
		return false
	}

	mp1 := make(map[byte]string)
	mp2 := make(map[string]byte)

	// Iterating over pattern and if there is same pattern make sure if match
	for i := range len(pattern) {
		if val, notEmpty := mp1[pattern[i]]; !notEmpty {
			mp1[pattern[i]] = strs[i]
			_, nE := mp2[strs[i]]
			// In case we got the value in the other map and is not the pattern we know is false
			if !nE {
				mp2[strs[i]] = pattern[i]
			} else if mp2[strs[i]] != pattern[i] {
				return false
			}
			// If the different
		} else if val != strs[i] {
			fmt.Println(val, "-", strs[i])
			return false
		}
	}
	fmt.Println(strs)
	// Compare by hashing
	return true
}

// Saving words in an array to compare later
func getWords(s string) []string {
	word := ""
	var strings []string
	for i := range len(s) {
		if s[i] != ' ' {
			word += string(s[i])
		}
		if s[i] == ' ' {
			strings = append(strings, word)
			word = ""
		}
	}
	strings = append(strings, word)
	return strings
}
