package main

func dailyTemperatures(temperatures []int) []int {
	result := make([]int, len(temperatures))
	stack := []int{}
	for i := 0; i < len(temperatures); i++ {
		// If stack is not empty and top of the stack is smaller than the actual temperature
		for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]] {
			top := stack[len(stack)-1]   // Top
			stack = stack[:len(stack)-1] // Pop
			result[top] = i - top
		}
		stack = append(stack, i)
	}
	return result
}

// My solution NOT EFFICIENT
func DdailyTemperatures(temperatures []int) []int {
	p1, p2 := 0, 1
	var days []int
	for p1 < len(temperatures) {
		if p2 >= len(temperatures) {
			days = append(days, 0)
			p1++
			p2 = p1 + 1
			continue
		}
		if temperatures[p1] < temperatures[p2] {
			days = append(days, p2-p1)
			p1++
			p2 = p1 + 1
		} else {
			p2++
		}
	}
	return days
}
