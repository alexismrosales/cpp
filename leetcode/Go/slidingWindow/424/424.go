package main

func characterReplacement(s string, k int) int {
	p1, maxFreq, maxLength := 0, 0, 0
	freq := make(map[byte]int)
	for p2 := 0; p2 < len(s); p2++ {
		freq[s[p2]]++
		maxFreq = max(maxFreq, freq[s[p2]])
		// if the number of replaces is bigger than k, it means it is not allowed
		if (p2-p1+1)-maxFreq > k {
			freq[s[p1]]--
			p1++
		}
		maxLength = max(maxLength, p2-p1+1)
	}
	return maxLength
}

func max(val1, val2 int) int {
	if val1 > val2 {
		return val1
	}
	return val2
}
