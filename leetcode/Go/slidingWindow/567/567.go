package main

func checkInclusion(s1 string, s2 string) bool {
	s1Map := make(map[byte]int)
	for i := 0; i < len(s1); i++ {
		s1Map[s1[i]]++
	}
	windowMap := make(map[byte]int)
	for p1, p2 := 0, 0; p2 < len(s2); p2++ {
		// Making window wider
		windowMap[s2[p2]]++
		// In case the window is bigger than s1 size
		if p2-p1 > len(s1) {
			if windowMap[s2[p1]] == 1 {
				delete(windowMap, s2[p1])
			} else {
				windowMap[s2[p1]]--
			}
			p1++
		}
		if isEqualMaps(s1Map, windowMap) {
			return true
		}
	}
	return false
}

// Comparing two frequences
func isEqualMaps(m1, m2 map[byte]int) bool {
	if len(m1) != len(m2) {
		return false
	}
	for k, v := range m1 {
		if m2[k] != v {
			return false
		}
	}
	return true
}
