package main

type Stack []byte

func (s *Stack) empty() bool {
	return len(*s) == 0
}
func (s *Stack) push(val byte) {
	*s = append(*s, val)
}

func (s *Stack) pop() byte {
	if s.empty() {
		return 'e'
	}
	top := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return top
}

func isValid(s string) bool {
	var stk Stack
	if len(s) == 1 {
		return false
	}
	for i := range len(s) {
		// In case if there is an open bracket
		if s[i] == '(' || s[i] == '{' || s[i] == '[' {
			stk.push(s[i])
		} else {
			val := stk.pop()
			// Finding their pairs
			switch s[i] {
			case ')':
				if val != '(' {
					return false
				}
			case '}':
				if val != '{' {
					return false
				}
			case ']':
				if val != '[' {
					return false
				}
			default:
				// If there is no open bracket
				if val == 'e' {
					return false
				}
			}
		}
	}
	// The stack can be not empty in that case there is not a match with all open brackets
	if !stk.empty() {
		return false
	}
	return true
}
