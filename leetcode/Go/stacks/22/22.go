package main

type Stack struct {
	parenthesis string
}

func (s *Stack) push(val string) {
	s.parenthesis += val
}

func (s *Stack) pop() {
	if len(s.parenthesis) == 0 {
		return
	}
	s.parenthesis = s.parenthesis[:len(s.parenthesis)-1]
}
func (s *Stack) lastElement() string {
	if len(s.parenthesis) == 0 {
		return ""
	}
	return string(s.parenthesis[len(s.parenthesis)-1])
}

func generateParenthesis(n int) []string {
	var solutions []string
	openB, closeB := n, n
	stack := &Stack{}
	recursiveGeneration(&openB, &closeB, stack, &solutions)
	return solutions
}

func recursiveGeneration(openB, closeB *int, stack *Stack, solutions *[]string) {
	// Returns if a left bracket counter is bigger thant close bracket is a non valid combination
	if *openB > *closeB {
		return
	}
	// In case we complete all brackets
	if *openB == 0 && *closeB == 0 {
		*solutions = append(*solutions, stack.parenthesis)
		return
	}
	// Pushing open bracket
	if *openB > 0 {
		stack.push("(")
		*openB--
		recursiveGeneration(openB, closeB, stack, solutions)
		// Restoring it state
		*openB++
	}
	// Pushing close bracket
	if *closeB > 0 {
		stack.push(")")
		*closeB--
		recursiveGeneration(openB, closeB, stack, solutions)
		// Restoring it state
		*closeB++
	}
	// Back to last state
	stack.pop()
}
