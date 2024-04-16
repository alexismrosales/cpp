package main

type stack []string

func reverseWords(s string) string {
	strings := saveWords(s)
	new := ""
	for i := len(strings) - 1; i > 0; i-- {
		if len(strings[i]) != 0 {
			new += strings[i] + " "
		}
	}
	return new
}

func saveWords(str string) []string {
	var strings []string
	word := ""
	for i := range len(str) {
		if str[i] != ' ' {
			word += string(str[i])
		} else {
			strings = append(strings, word)
			word = ""
		}
	}
	strings = append(strings, word)
	return strings
}

func (s *stack) Push(str string) {
	*s = append(*s, str)
}

func (s *stack) Pop() string {
	l := len(*s)
	if l == 0 {
		return "$"
	}
	popped := (*s)[l-1]
	*s = (*s)[:l-1]
	return popped
}
