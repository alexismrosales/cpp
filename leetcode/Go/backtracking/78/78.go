package main

func subsets(nums []int) [][]int {
	var subsetsAns [][]int
	var current []int
	var generateSubsets func(start int)
	generateSubsets = func(start int) {
		// Saving every result of current
		temp := make([]int, len(current))
		copy(temp, current)
		subsetsAns = append(subsetsAns, temp)
		// Recursion ends when start value reach size of nums
		if start == len(nums) {
			return
		}
		// Starting from start so digits do not repeat
		for i := start; i < len(nums); i++ {
			current = append(current, nums[i])
			generateSubsets(i + 1)
			current = current[:len(current)-1]
		}
	}
	generateSubsets(0)
	return subsetsAns
}
