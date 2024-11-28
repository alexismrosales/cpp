package main

func combinationSum(candidates []int, target int) [][]int {
	var combinations [][]int
	var current []int
	var backtrack func(start, sum int)

	backtrack = func(start, sum int) {
		// Condition to end recursion
		// If the target is reached
		if sum == target {
			temp := make([]int, len(current))
			copy(temp, current)
			combinations = append(combinations, temp)
			return
		}
		// If the sum is bigger
		if sum > target {
			return
		}
		for i := start; i < len(candidates); i++ {
			current = append(current, candidates[i])
			backtrack(i, sum+candidates[i])
			current = current[:len(current)-1]
		}

	}
	backtrack(0, 0)
	return combinations
}
