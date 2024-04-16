package main

func isIsomorphic(s string, t string) bool {
	m1 := make(map[byte]byte)
	m2 := make(map[byte]byte)

	for i := range len(s) {
		if val1, notEmpty := m1[s[i]]; !notEmpty {
			m1[s[i]] = t[i]
			val2, nE := m2[t[i]]
			if !nE {
				m2[t[i]] = s[i]
			} else if val2 != s[i] {
				return false
			}
		} else if val1 != t[i] {
			return false
		}
	}
	return true
}
