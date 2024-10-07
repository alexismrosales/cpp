package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	lettersS := make(map[byte]int)
	lettersT := make(map[byte]int)
	// Saving letters in the map
	for i := range len(s) {
		lettersS[s[i]] = lettersS[s[i]] + 1
		lettersT[t[i]] = lettersT[t[i]] + 1
	}
	for j := range len(t) {
		// If the size of letters is different
		if lettersS[t[j]] != lettersT[t[j]] {
			return false
		}

		// Cheking if the other words have the same letters
		if _, exists := lettersS[t[j]]; !exists {
			return false
		}
	}
	return true
}
