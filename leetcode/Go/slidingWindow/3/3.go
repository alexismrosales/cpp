package main

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	if len(s) == 1 {
		return 1
	}
	substring := make(map[byte]struct{})
	sb := ""
	longest := ""
	i, j := 0, 1
	// Adding first element to the substring map
	substring[s[i]] = struct{}{}
	sb = string(s[i])
	for j < len(s) {
		if _, exist := substring[s[j]]; exist {

			// Assign of longest substring
			if len(sb) > len(longest) {
				longest = sb
			}
			// Reset of substring
			i++
			j = i + 1
			substring = make(map[byte]struct{})
			substring[s[i]] = struct{}{}
			sb = string(s[i])
		} else {
			// Add character to map
			substring[s[j]] = struct{}{}
			// Add character to substring string
			sb = sb + string(s[j])
			j++
		}
	}
	if len(longest) == 0 {
		return len(s)
	}
	return len(longest)
}
